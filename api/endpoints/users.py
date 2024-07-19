from fastapi import APIRouter, Depends
from dependencies import get_current_active_user
from schemas import User
from sqlalchemy.orm import Session
import schema.user_schema as schemas
from . import crud
from typing import Annotated
from database import get_dbase

db_dependecy = Annotated[Session, Depends(get_dbase)]

router = APIRouter()


@router.get("/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.post("", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: db_dependecy):
    return crud.create_user(db=db, user=user)


@router.post("/login", response_model=schemas.User)
def login_user(user: schemas.UserLogin, db: db_dependecy):
    return crud.login_user(db=db, email=user.email, password=user.password)


@router.put("/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: db_dependecy):
    return crud.update_user(db=db, user_id=user_id, user=user)


@router.delete("/{user_id}")
def delete_user(user_id: int, db: db_dependecy):
    return crud.delete_user(db=db, user_id=user_id)


@router.post("/change-password/{user_id}", response_model=schemas.User)
def change_password(user_id: int, password: schemas.PasswordChange,
                    db: db_dependecy):
    return crud.change_password(db=db,
                                user_id=user_id,
                                old_password=password.old_password,
                                new_password=password.new_password)


@router.post("/forgot-password")
def forgot_password(email: str, db: db_dependecy):
    return crud.forgot_password(db=db, email=email)
