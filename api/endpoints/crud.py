from sqlalchemy.orm import Session
import schema.user_schema as schemas
import models
import smtplib


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, email=user.email)
    db_user.set_password(user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def login_user(db: Session, email: str, password: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if user and user.check_password(password):
        return user
    return None


def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(models.User).get(user_id)
    if db_user:
        if user.username:
            db_user.username = user.username
        if user.email:
            db_user.email = user.email
        if user.password:
            db_user.set_password(user.password)
        db.commit()
        db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).get(user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return {"message": f"User with id {user_id} deleted"}


def change_password(db: Session, user_id: int, old_password: str,
                    new_password: str):
    db_user = db.query(models.User).get(user_id)
    if db_user and db_user.check_password(old_password):
        db_user.set_password(new_password)
        db.commit()
        db.refresh(db_user)
        return db_user
    return None


def forgot_password(db: Session, email: str):
    db_user = db.query(models.User).filter(models.User.email == email).first()
    if db_user:
        # Send password reset email to the user
        try:
            smtp_server = smtplib.SMTP('localhost')
            reset_link = f"https://example.com/reset-password?user_id={db_user.id}"
            message = f"Reset your password by clicking this link: {reset_link}"
            smtp_server.sendmail('from@example.com', email, message)
            print(f"Password reset link sent to {email}")
        except Exception as e:
            print(f"Error sending email: {e}")
    return {"message": f"Password reset link sent to {email}"}
