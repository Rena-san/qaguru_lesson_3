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