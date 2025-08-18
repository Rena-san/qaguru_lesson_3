# from fastapi import FastAPI, HTTPException, status
# from fastapi_pagination import add_pagination
# from fastapi import Query
# from app.models.user_data import users_list
# from app.models.models import UsersResponseModel, ResponseModel
#
# USERS = users_list()
#
# app = FastAPI()
# add_pagination(app)
#
#
# @app.get("/status")
# def health_check():
#     return {"status": "ok"}
#
#
# @app.get("/users", response_model=UsersResponseModel)
# def get_users(
#         page: int = Query(1, ge=1),
#         size: int = Query(10, ge=1, le=100),
# ):
#     start = (page - 1) * size
#     end = start + size
#     users_page = USERS[start:end]
#     return {
#         "data": users_page,
#         "total": len(USERS),
#         "page": page,
#         "size": size
#     }
#
#
# @app.get("/users/{user_id}", response_model=ResponseModel)
# def get_user_or_404(user_id: int):
#     for user in USERS:
#         if user["id"] == user_id:
#             return {
#                 "data": user
#             }
#     else:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail={"error": "User not found", "user_id": user_id}
#         )

import dotenv

dotenv.load_dotenv()


import uvicorn
from fastapi import FastAPI

from routers import status, users
from app.database.engine import create_db_and_tables


app = FastAPI()
app.include_router(status.router)
app.include_router(users.router)


if __name__ == "__main__":
    create_db_and_tables()
    uvicorn.run(app, host="localhost", port=8002)