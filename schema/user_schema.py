from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserUpdate(BaseModel):
    username: str | None = None
    email: str | None = None
    password: str | None = None


class PasswordChange(BaseModel):
    old_password: str
    new_password: str


class User(UserBase):
    id: int
    is_active: bool

    # class Config:
    #     from_attributes = True
