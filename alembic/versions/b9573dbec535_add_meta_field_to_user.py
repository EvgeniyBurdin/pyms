"""Add meta field to user

Revision ID: b9573dbec535
Revises: 9f403d5eb0bd
Create Date: 2020-09-18 17:40:38.906155

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b9573dbec535'
down_revision = '9f403d5eb0bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('meta', postgresql.JSONB(astext_type=sa.Text()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'meta')
    # ### end Alembic commands ###
