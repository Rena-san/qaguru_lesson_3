from http import HTTPStatus
from math import ceil
from sqlalchemy import func

from fastapi import APIRouter, Query, Depends
from sqlmodel import Session, select

from typing import Iterable

from fastapi import APIRouter, HTTPException
from pydantic_core._pydantic_core import ValidationError

from app.database import users
from app.database.engine import get_session
from app.models.User import User, UserCreate, UserUpdate, PageUsers

router = APIRouter(prefix="/api/users")


@router.get("/{user_id}", status_code=HTTPStatus.OK)
def get_user(user_id: int) -> User:
    if user_id < 1:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="Invalid user id")
    user = users.get_user(user_id)

    if not user:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    return user


# @router.get("/", status_code=HTTPStatus.OK)
# def get_users() -> Iterable[User]:
#     return users.get_users()

@router.get("/", status_code=HTTPStatus.OK, response_model=PageUsers)
def get_users(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    session: Session = Depends(get_session),
) -> PageUsers:
    total = session.exec(select(func.count()).select_from(User)).one()
    offset = (page - 1) * size
    items = session.exec(select(User).offset(offset).limit(size)).all()
    pages = ceil(total / size) if total else 1
    return PageUsers(items=items, total=total, page=page, size=size, pages=pages)


@router.post("/", status_code=HTTPStatus.CREATED)
def create_user(user: User) -> User:
    try:
        validated = UserCreate.model_validate(user.model_dump())
    except ValidationError as e:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail=e.errors())

    if not validated.first_name.strip() or not validated.last_name.strip():
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                            detail="first_name and last_name cannot be empty")

    return users.create_user(user)


@router.patch("/{user_id}", status_code=HTTPStatus.OK)
def update_user(user_id: int, user: User) -> User:
    if user_id < 1:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="Invalid user id")

    existing_user = users.get_user(user_id)
    if not existing_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )

    UserUpdate.model_validate(user.model_dump())
    return users.update_user(user_id, user)


@router.delete("/{user_id}", status_code=HTTPStatus.OK)
def delete_user(user_id: int):
    if user_id < 1:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="Invalid user id")

    existing_user = users.get_user(user_id)
    if not existing_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )

    users.delete_user(user_id)
    return {"message": "User deleted"}