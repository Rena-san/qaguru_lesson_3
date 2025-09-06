import allure
import api_requests.api as api
from app.models.User import UserCreate
from utils.utiles import generate_email, generate_name, generate_avatar_link


def get_user_data():
    with allure.step("Prepare user data"):
        user = UserCreate(
            email=generate_email(),
            first_name=generate_name(),
            last_name=generate_name(),
            avatar=generate_avatar_link()
        )
        return user


def create_user():
    user = get_user_data()
    with allure.step("Create user"):
        response = api.create_user(user)
    return response
