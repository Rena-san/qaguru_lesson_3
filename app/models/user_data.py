import json
import os

from app.models.User import UserCreate

CONFIG_PATH = '/users.json'
DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def users_list():
    with open(DIR_PATH + CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


def create_user_data(user_id):
    user_list = users_list()
    for user in user_list:
        if user['id'] == user_id:
            return UserCreate(**user)

