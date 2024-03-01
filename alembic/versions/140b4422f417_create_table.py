"""create table
Revision ID: 140b4422f417
Revises: 
Create Date: 2024-03-01 14:47:58.221772

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '140b4422f417'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name',sa.String(), nullable=False),
        sa.Column('age',sa.String(), nullable=False)
        

    )
    

def downgrade() -> None:
    pass
