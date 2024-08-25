"""misc

Revision ID: 4984cf81e7b9
Revises: 3b56576fb4ed
Create Date: 2024-08-25 04:05:01.432234

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "4984cf81e7b9"
down_revision: Union[str, None] = "3b56576fb4ed"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "project_credential",
        sa.Column("project_id", sa.UUID(), nullable=True),
        sa.Column("credential_id", sa.UUID(), nullable=True),
        sa.ForeignKeyConstraint(
            ["credential_id"],
            ["credentials.id"],
        ),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.id"],
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("project_credential")
    # ### end Alembic commands ###
