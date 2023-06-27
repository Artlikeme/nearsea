from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey, TIMESTAMP

from src.auth.models import user
from src.database import metadata

city = Table(
    'city',
    metadata,
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
    Column("check-in", TIMESTAMP),
    Column("departure", TIMESTAMP),
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
    Column("apartment_rule_id", Integer, ForeignKey(apartment_rule.c.id)),
)

booking = Table(
    'booking',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("rating", String, nullable=True),
    Column("status", String, nullable=True),
    Column("start", TIMESTAMP),
    Column("end", TIMESTAMP),
    Column("price", Integer),
    Column("paid_price", Integer),
    Column("created_at", TIMESTAMP, default=datetime.utcnow),
    Column("apartment_id", Integer, ForeignKey(apartment.c.id)),
    Column("user_id", Integer, ForeignKey(user.c.id)),
)
