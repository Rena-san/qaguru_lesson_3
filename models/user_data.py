import json
import os

USER_DATA_REQRES = {
    "email": "eve.holt@reqres.in",
    "password": "pistol",
}

CONFIG_PATH = '/users.json'
DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def users_list():
    with open(DIR_PATH + CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data
