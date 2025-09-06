from http import HTTPStatus

import allure

from steps import steps
from api_requests import api as api
from utils.utiles import generate_email


def test_create_user():
    user = steps.get_user_data()
    with allure.step("Create user"):
        resp = api.create_user(user)
        assert resp.status_code == HTTPStatus.CREATED

def test_delete_user():
    res = steps.create_user()
    with allure.step("Delete user"):
        user_id = res.json()["id"]
        resp = api.delete_user(user_id)
        assert resp.status_code == HTTPStatus.OK

def test_user_was_deleted():
    res = steps.create_user()

    with allure.step("Delete user"):
        user_id = res.json()["id"]
        api.delete_user(user_id)

    with allure.step("Check that user was deleted"):
        resp = api.get_user(user_id)
        assert resp.status_code == HTTPStatus.NOT_FOUND

def test_update_user():
    user = steps.get_user_data()

    with allure.step("Create user"):
        resp = api.create_user(user)

    with allure.step("Update user email"):
        user_id = resp.json()["id"]
        new_email = generate_email()
        user.email = new_email
        resp = api.update_user(user_id, user)
        assert resp.status_code == HTTPStatus.OK
        assert resp.json()["email"] == new_email
        user_info_after_update = api.get_user(user_id)
        assert user_info_after_update.json()["email"] == new_email

def test_unable_to_update_user_with_wrong_user_id():
    user = steps.get_user_data()

    with allure.step("Create user"):
        resp = api.create_user(user)
    with allure.step("Update user email with wrong user_id"):
        not_existing_user_id = 100
        new_email = generate_email()
        user.email = new_email
        resp = api.update_user(not_existing_user_id, user)
        assert resp.status_code == HTTPStatus.NOT_FOUND

def test_method_not_allowed():
    with allure.step("Send wring request"):
        resp = api.send_wrong_request()
        assert resp.status_code == HTTPStatus.METHOD_NOT_ALLOWED

def test_unable_to_delete_user_with_not_existing_user_id():
    not_existing_user_id = 100
    resp = api.delete_user(not_existing_user_id)
    assert resp.status_code == HTTPStatus.NOT_FOUND


def test_unable_to_delete_user_with_invalid_user_id():
    invalid_user_id = 'a'
    resp = api.delete_user(invalid_user_id)
    assert resp.status_code == HTTPStatus.UNPROCESSABLE_ENTITY

def test_unable_to_update_user_with_invalid_user_id():
    user = steps.get_user_data()
    with allure.step("Create user"):
        res = api.create_user(user)
    with allure.step("Update user with invalid user_id"):
        user.email = generate_email()
        invalid_user_id = 's'
        resp = api.update_user(invalid_user_id, user)
        assert resp.status_code == HTTPStatus.UNPROCESSABLE_ENTITY

def test_user_flow():
    user = steps.get_user_data()
    with allure.step("Create user"):
        resp = api.create_user(user)
        assert resp.status_code == HTTPStatus.CREATED

    with allure.step("Get user"):
        user_id = resp.json()["id"]
        resp = api.get_user(user_id)
        assert resp.status_code == HTTPStatus.OK

    with allure.step("Update user"):
        user.email = 'test@example.com'
        resp = api.update_user(user_id, user)
        assert resp.status_code == HTTPStatus.OK

    with allure.step("Delete user"):
        resp = api.delete_user(user_id)
        assert resp.status_code == HTTPStatus.OK

def test_unable_to_create_user_with_invalid_email():
    user = steps.get_user_data()
    user.email = "email.emal.com"
    with allure.step("Create user"):
        resp = api.create_user(user)
        assert resp.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
        assert resp.json()['detail'][0].get("msg") == "value is not a valid email address: An email address must have an @-sign."


def test_unable_to_create_user_with_empty_name():
    user = steps.get_user_data()
    user.first_name = ""
    user.last_name = ""

    with allure.step("Create user"):
        resp = api.create_user(user)
        assert resp.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
        assert resp.json()['detail'] == 'first_name and last_name cannot be empty'
