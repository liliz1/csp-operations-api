from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = (
    "postgresql+psycopg://"
    "csp_user:csp_password@localhost:5432/csp_db"
)

engine = create_engine(
    DATABASE_URL, 
    echo=True,
)

class Base(DeclarativeBase):
    pass

