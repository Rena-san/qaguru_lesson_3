import logging
import requests

from utils.utiles import Api


def user_registration(user_data):
    url = f"{Api.HOST}/api/register"

    headers = {
        "x-api-key": "reqres-free-v1"
    }

    body = {
        "email": user_data.email,
        "password": user_data.password,
    }

    logging.info(f"POST->URL::{url}")
    logging.info(f"POST->BODY::{body}")

    response = requests.post(url, headers=headers, json=body)

    logging.info(f"RESPONSE::{response.json()}")

    return response


def user_login(user_data):
    url = f"{Api.HOST}/api/login"

    headers = {
        "x-api-key": "reqres-free-v1"
    }

    body = {
        # "username": models.username,
        "email": user_data.email,
        "password": user_data.password,
    }

    logging.info(f"POST->URL::{url}")
    logging.info(f"POST->BODY::{body}")

    response = requests.post(url, headers=headers, json=body)

    logging.info(f"RESPONSE::{response.json()}")

    return response
