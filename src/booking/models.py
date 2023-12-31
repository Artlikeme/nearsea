import enum
from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey, TIMESTAMP, Enum, Time

from src.auth.models import user
from src.database import metadata

# классический способ задания моделей
city = Table(
    'city',
    metadata,
    Column("id", Integer, primary_key=True),
    Column('name', String)
)

type_apartment = Table(
    'type_apartment',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
)

tag = Table(
    'tag',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("description", String),
    Column("image", String, nullable=True),
)

apartment_rule = Table(
    'apartment_rule',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("check-in", Time),
    Column("departure", Time),
    Column("min_days", Integer, default=1),
)

price = Table(
    'price',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("start", TIMESTAMP),
    Column("end", TIMESTAMP),
    Column("price", Integer),
)

apartment = Table(
    'apartment',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("description", String),
    Column("image", String, nullable=True),
    Column("address", String),
    Column("rating", Integer, default=0, nullable=True),
    Column("distance_to_sea", Integer),
    Column("ia_active", Boolean, default=False),
    Column("added_at", TIMESTAMP, default=datetime.utcnow),
    Column("quantity_room", Integer, nullable=True),
    Column("square", Integer),
    Column("pledge", Integer),  # залог
    Column("max_num_of_guests", Integer),
    Column("storey_of_house", Integer, nullable=True),  # кол-во этажей в доме
    Column("storey", Integer),  # этаж
    Column("type_id", Integer, ForeignKey(type_apartment.c.id)),
    Column("user_id", Integer, ForeignKey(user.c.id)),
    Column("tags_id", Integer, ForeignKey(tag.c.id)),
    Column("city_id", Integer, ForeignKey(city.c.id)),
    Column("apartment_rule_id", Integer, ForeignKey(apartment_rule.c.id)),
)


class StatusEnum(enum.Enum):
    first = 'Ожидает оплаты'
    second = 'Оплачена'
    third = 'Отменена'


booking = Table(
    'booking',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("rating", String, default=0, nullable=True),
    Column("status", Enum(StatusEnum)),
    Column("start", TIMESTAMP),
    Column("end", TIMESTAMP),
    Column("price", Integer),
    Column("paid_price", Integer, default=0, nullable=True),
    Column("created_at", TIMESTAMP, default=datetime.utcnow),
    Column("apartment_id", Integer, ForeignKey(apartment.c.id)),
    Column("user_id", Integer, ForeignKey(user.c.id)),
)
