"""create table

Revision ID: 05882e04c509
Revises: 140b4422f417
Create Date: 2024-03-01 14:49:39.528379

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '05882e04c509'
down_revision: Union[str, None] = '140b4422f417'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
