import http

from reqres.api_calls import user_registration, user_login
import allure


def test_user_registration(user_data):
    with allure.step("Send user registration request"):
        response = user_registration(user_data)

        with allure.step("Assert status code"):
            assert response.status_code == http.HTTPStatus.OK.value

        with allure.step("Assert response contains user id"):
            assert response.json().get("id") != "", "User id field is empty"

        with allure.step("Assert response contains token"):
            assert response.json().get("token") != "", "User token field is empty"


def test_successful_user_login(user_data):
    with allure.step("User login"):
        response = user_login(user_data)

        with allure.step("Assert status code"):
            assert response.status_code == http.HTTPStatus.OK.value

        with allure.step("Assert response contains token"):
            assert response.json().get("token"), "Response should contain token"


def test_unsuccessful_user_login_with_empty_password(user_data):
    with allure.step("Preconditions"):
        user_data.password = ""

    with allure.step("User login"):
        response = user_login(user_data)

        with allure.step("Assert status code"):
            assert response.status_code == http.HTTPStatus.BAD_REQUEST.value
