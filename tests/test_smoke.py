from app.api import check_status, get_user, get_users
from http import HTTPStatus


def test_check_status():
    response = check_status()
    assert response.status_code == HTTPStatus.OK
    # assert response.json()["status"] == "ok"

def test_check_users_status():
    response = get_users()
    assert response.status_code == HTTPStatus.OK

def test_check_user_status(user_id=3):
    response = get_user(user_id)
    assert response.status_code == HTTPStatus.OK
