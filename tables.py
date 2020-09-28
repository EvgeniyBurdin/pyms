""" Схема базы данных в формате sqlalchemy-core.
"""
from sqlalchemy import (BigInteger, Column, DateTime, ForeignKey, MetaData,
                        String, Table, func)
from sqlalchemy.dialects.postgresql import JSONB, UUID

metadata = MetaData()


def get_tables() -> dict:
    return metadata.tables


user = Table(
    "user", metadata,

    Column(
        "id", UUID, primary_key=True, server_default=func.uuid_generate_v4(),
    ),
    Column(
        "name", String, nullable=False,
    ),
    Column(
        "birth_date", DateTime(timezone=True), nullable=True,
    ),
    Column(
        "meta", JSONB, nullable=True,
    ),
)


email = Table(
    "email", metadata,

    Column(
        "id", BigInteger, primary_key=True, autoincrement=True
    ),
    Column(
        "address", String, nullable=False
    ),
    Column(
        "user_id", UUID, ForeignKey('user.id'), nullable=False,
    ),
)


team = Table(
    "team", metadata,

    Column(
        "id", BigInteger, primary_key=True, autoincrement=True,
    ),
    Column(
        "name", String, nullable=False
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


users_in_teams = Table(
    "users_in_teams", metadata,

    Column(
        "user_id", UUID, ForeignKey('user.id'), nullable=False,
        primary_key=True,
    ),
    Column(
        "team_id", BigInteger, ForeignKey('team.id'), nullable=False,
        primary_key=True,
    )
)
