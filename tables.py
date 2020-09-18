""" Схема базы данных.
"""
from sqlalchemy import (BigInteger, Column, DateTime, MetaData, String, Table,
                        func)
from sqlalchemy.dialects.postgresql import JSONB, UUID

metadata = MetaData()


user = Table(

    "user", metadata,

    Column(
        "id", UUID, primary_key=True, server_default=func.uuid_generate_v4()
    )
)

phone = Table(

    "phone", metadata,

    Column(
        Column("id", BigInteger, primary_key=True, autoincrement=True),
    )
)

team = Table(

    "team", metadata,

    Column(
        Column("id", BigInteger, primary_key=True, autoincrement=True),
    )
)

users_in_teams = Table(

    "users_in_teams", metadata,

    Column(
        Column("id", BigInteger, primary_key=True, autoincrement=True),
    )
)


people = Table(

    "people", metadata,

    Column(
        "id", UUID, primary_key=True, server_default=func.uuid_generate_v4()
    ),
    Column(
        "name", String, nullable=False
    ),
    Column(
        "extra", JSONB
    ),
    Column(
        "created", DateTime(timezone=True), nullable=False,
        server_default=func.now()
    ),
    Column(
        "updated", DateTime(timezone=True), nullable=True,
        onupdate=func.now()
    ),
)
