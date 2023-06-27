from datetime import date

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    pass


class UserCreate(schemas.BaseUserCreate):
    id: int
    username: str
    registered_at: str


class UserUpdate(schemas.BaseUserUpdate):
    pass