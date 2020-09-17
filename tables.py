""" Схема базы данных.
"""
from sqlalchemy import Column, DateTime, MetaData, String, Table, func
from sqlalchemy.dialects.postgresql import JSONB, UUID

metadata = MetaData()


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
