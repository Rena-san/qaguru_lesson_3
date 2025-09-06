import random
import string


class Api:
    HOST = "https://reqres.in"
    LOCAL_HOST = "http://localhost:8000"


def generate_email(prefix="qatest_") -> str:
    name = "".join(random.choices(string.digits, k=5))
    return f"{prefix}{name}@example.com"

def generate_name() -> str:
    return "".join(random.choices(string.ascii_uppercase , k=5))

def generate_avatar_link(img_name='image'):
    return f"{Api.LOCAL_HOST}/img/faces/{img_name}.jpg"
