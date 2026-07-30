from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings

# DATABASE_URL = (
#     "postgresql+psycopg://"
#     "csp_user:csp_password@localhost:5432/csp_db"
# )
DATABASE_URL = (
    f"postgresql+psycopg://{settings.postgres_user}:"
    f"{settings.postgres_password}@{settings.postgres_host}:"
    f"{settings.postgres_port}/{settings.postgres_db}"
)

engine = create_engine(
    DATABASE_URL, 
    echo=True,
)

class Base(DeclarativeBase):
    pass


