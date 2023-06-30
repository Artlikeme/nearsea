from datetime import datetime
from enum import Enum

from pydantic import BaseModel

from src.auth.shemas import UserRead
from src.booking.models import StatusEnum


class Apartment(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True


class ApartmentCreate(BaseModel):
    name: str
    description: str
    image: str
    address: str
    distance_to_sea: int
    type_id: int
    user_id: int
    tags_id: int
    apartment_rule_id: int
    square: int
    pledge: int
    max_num_of_guests: int
    storey: int


class UserApartments(Apartment):
    user_id: int
    # class Config:
    #     orm_mode = True


class Status(str, Enum):
    first = 'Ожидает оплаты'
    second = 'Оплачена'
    third = 'Отменена'


class BookingRead(BaseModel):
    id: int
    status: StatusEnum
    rating: str
    start: datetime
    end: datetime
    price: int
    paid_price: int
    created_at: datetime
    apartment_id: int
    user_id: int

    class Config:
        orm_mode = True


class BookingCreate(BaseModel):
    status: StatusEnum
    start: datetime
    end: datetime
    price: int
    apartment_id: int
    user_id: int
