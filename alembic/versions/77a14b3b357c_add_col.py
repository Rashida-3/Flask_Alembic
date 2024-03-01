"""add col

Revision ID: 77a14b3b357c
Revises: 05882e04c509
Create Date: 2024-03-01 16:13:36.660531

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '77a14b3b357c'
down_revision: Union[str, None] = '05882e04c509'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'id',
        sa.Column('username',sa.String)
    )


def downgrade() -> None:
    op.drop_column('id','username')
