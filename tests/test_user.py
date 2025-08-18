import http
import pytest

import allure
# from app.api import get_users, get_user
from app.models.user_data import users_list, create_user_data
from app import api as api

USERS = users_list()


def test_create_user():
    user = create_user_data(1)
    resp = api.create_user(user)
    assert resp.status_code == 201

# def test_get_all_users():
#     with allure.step("Get all users"):
#         response = get_users()
#         with allure.step("Assert status code"):
#             assert response.status_code == http.HTTPStatus.OK.value
#         with allure.step("Assert users quantity"):
#             users_quantity = 12
#             assert response.json().get("total") == users_quantity, "Incorrect number of users"
#
# @pytest.mark.parametrize("user_id", [2, 5, 10])
# def test_get_user(user_id):
#     with allure.step("Get user"):
#         response = get_user(user_id)
#         with allure.step("Assert status code"):
#             assert response.status_code == http.HTTPStatus.OK.value
#         with allure.step("Assert user email"):
#             assert response.json().get("data").get("email") == USERS[user_id-1].get("email"), "Incorrect email"



