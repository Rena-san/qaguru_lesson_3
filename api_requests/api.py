import logging

import requests

from utils.utiles import Api


def get_users(page=1, size=10):
    url = f"{Api.LOCAL_HOST}/api/users?page={page}&size={size}"

    logging.info(f"GET->URL::{url}")

    response = requests.get(url)

    logging.info(f"RESPONSE::{response.json()}")

    return response


def get_user(user_id):
    url = f"{Api.LOCAL_HOST}/api/users/{user_id}"

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
    logging.info(f"POST->DATA::{user.model_dump()}")

    response = requests.post(url, json=user.model_dump())

    logging.info(f"RESPONSE::{response.json()}")

    return response

def delete_user(user_id):
    url = f"{Api.LOCAL_HOST}/api/users/{user_id}"

    logging.info(f"DELETE->URL::{url}")

    response = requests.delete(url)

    logging.info(f"RESPONSE::{response.json()}")

    return response

def update_user(user_id, user):
    url = f"{Api.LOCAL_HOST}/api/users/{user_id}"

    logging.info(f"PATCH->URL::{url}")
    logging.info(f"PATCH->DATA::{user.model_dump()}")

    response = requests.patch(url, json=user.model_dump())

    logging.info(f"RESPONSE::{response.json()}")

    return response

def send_wrong_request():
    url = f"{Api.LOCAL_HOST}/api/users"

    response = requests.delete(url)
    logging.info(f"RESPONSE::{response.json()}")
    return response