from pydantic import BaseModel, EmailStr, HttpUrl

from models.user_data import USER_DATA_REQRES


class User(BaseModel):
    password: str = None
    email: EmailStr = None


def get_user():
    return User(**USER_DATA_REQRES)


class UserData(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    avatar: HttpUrl


class SupportData(BaseModel):
    url: str
    text: str


class UsersResponseModel(BaseModel):
    data: list[UserData]
    total: int
    page: int
    size: int


class ResponseModel(BaseModel):
    data: UserData
