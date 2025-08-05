import logging

import pytest
from models.models import get_user


@pytest.fixture(scope="session")
def user_data():
    user = get_user()
    logging.info(f"USER DATA: {user.model_dump_json()}")
    return user