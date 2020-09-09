from sqlalchemy import Column, MetaData, String, Table, func
from sqlalchemy.dialects.postgresql import JSONB, UUID


metadata = MetaData()


tasks_table = Table(

    "pyms_people", metadata,

    Column(
        "id", UUID, primary_key=True, server_default=func.uuid_generate_v4()
    ),
    Column(
        "name", String, nullable=False
    ),
    Column(
        "extra", JSONB
    ),
)
