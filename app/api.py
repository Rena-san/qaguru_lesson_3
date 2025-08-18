import logging

import requests

from utils.utiles import Api


def get_users(page=1, size=10):
    url = f"{Api.LOCAL_HOST}/users?page={page}&size={size}"

    logging.info(f"GET->URL::{url}")

    response = requests.get(url)

    logging.info(f"RESPONSE::{response.json()}")

    return response


def get_user(user_id):
    url = f"{Api.LOCAL_HOST}/users/{user_id}"

    logging.info(f"GET->URL::{url}")

    response = requests.get(url)

    logging.info(f"RESPONSE::{response.json()}")

    return response

def check_status():
    url = f"{Api.LOCAL_HOST}/status"

    logging.info(f"GET->URL::{url}")

    response = requests.get(url)

    logging.info(f"RESPONSE::{response.json()}")

    return response

def create_user(user):
    url = f"{Api.LOCAL_HOST}/api/users/"
    logging.info(f"POST->URL::{url}")

    body = {
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "avatar": user.avatar,
    }

    logging.info(f"POST->DATA::{user.model_dump_json()}")
    response = requests.post(url, json=body)
    logging.info(f"RESPONSE::{response.json()}")
    return response