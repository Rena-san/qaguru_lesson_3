import math
import allure

from app.api import get_users
from http import HTTPStatus
import pytest


@pytest.mark.parametrize("size", [2, 5, 10])
def test_pagination_item_count(size):
    with allure.step("Getting page items count"):
        response = get_users(size=size)
        assert response.status_code == HTTPStatus.OK
        assert len(response.json()["data"]) == size


@pytest.mark.parametrize("size", [2, 4, 5])
def test_page_count_matches_total(size):
    with allure.step(f"Count all pages with size:{size}"):
        response = get_users(size=size)
        assert response.status_code == HTTPStatus.OK
        total = response.json()["total"]
        expected_pages = math.ceil(total / size)

    with allure.step("Check last page"):
        last_page = get_users(page=expected_pages, size=size)
        assert last_page.status_code == HTTPStatus.OK
        assert "data" in last_page.json()


def test_different_pages_return_different_data():
    with allure.step('Check pages contain different data'):
        page_1 = get_users(page=1, size=3)
        page_2 = get_users(page=2, size=3)
        assert page_1.status_code == HTTPStatus.OK and page_2.status_code == HTTPStatus.OK
        assert page_1.json()["data"] != page_2.json()["data"]
