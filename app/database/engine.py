import os

from sqlalchemy.orm import Session
from sqlmodel import create_engine, SQLModel, text



def _int_env(name: str, default: int) -> int:
    val = os.getenv(name)
    try:
        return int(val) if val is not None else default
    except ValueError:
        return default


engine = create_engine(os.getenv("DATABASE_ENGINE"), pool_size=_int_env(os.getenv("DATABASE_ENGINE"), 10))


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def check_availability() -> bool:
    try:
        with Session(engine) as session:
            session.execute(text("SELECT 1"))
        return True
    except Exception as e:
        print(e)
        return False