import datetime

from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Table, Column, Integer, String, Boolean

from src.database import Base, metadata

user = Table(
    'user',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, unique=True, nullable=False),
    Column("username", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("registered_at", String, default=datetime.datetime.utcnow()),
    Column("is_active", Boolean, default=False, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),

)


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    registered_at = Column(String, default=datetime.datetime.utcnow)
