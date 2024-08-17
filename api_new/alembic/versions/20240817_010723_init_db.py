"""init db

Revision ID: b5b95161115f
Revises:
Create Date: 2024-08-17 01:07:23.760329

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "b5b95161115f"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "organization_references",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_organization_references_created_at"),
        "organization_references",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        op.f("ix_organization_references_name"),
        "organization_references",
        ["name"],
        unique=False,
    )
    op.create_index(
        op.f("ix_organization_references_updated_at"),
        "organization_references",
        ["updated_at"],
        unique=False,
    )
    op.create_table(
        "user_references",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("google_id", sa.String(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_user_references_created_at"),
        "user_references",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        op.f("ix_user_references_email"), "user_references", ["email"], unique=True
    )
    op.create_index(
        op.f("ix_user_references_google_id"),
        "user_references",
        ["google_id"],
        unique=True,
    )
    op.create_index(
        op.f("ix_user_references_updated_at"),
        "user_references",
        ["updated_at"],
        unique=False,
    )
    op.create_table(
        "api_tokens",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("token", sa.String(), nullable=True),
        sa.Column("user_id", sa.UUID(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user_references.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_api_tokens_created_at"), "api_tokens", ["created_at"], unique=False
    )
    op.create_index(op.f("ix_api_tokens_token"), "api_tokens", ["token"], unique=True)
    op.create_index(
        op.f("ix_api_tokens_updated_at"), "api_tokens", ["updated_at"], unique=False
    )
    op.create_table(
        "projects",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("is_user_default", sa.Boolean(), nullable=True),
        sa.Column("organization_id", sa.UUID(), nullable=True),
        sa.Column("user_id", sa.UUID(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["organization_id"],
            ["organization_references.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user_references.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_projects_created_at"), "projects", ["created_at"], unique=False
    )
    op.create_index(op.f("ix_projects_name"), "projects", ["name"], unique=False)
    op.create_index(
        op.f("ix_projects_updated_at"), "projects", ["updated_at"], unique=False
    )
    op.create_table(
        "packages",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("project_id", sa.UUID(), nullable=True),
        sa.Column("type", sa.String(), nullable=True),
        sa.Column(
            "deploy_status",
            sa.Enum(
                "NOT_DEPLOYED", "DEPLOYING", "DEPLOYED", "FAILED", name="deploy_status"
            ),
            nullable=True,
        ),
        sa.Column("inputs", sa.JSON(), nullable=True),
        sa.Column("outputs", sa.JSON(), nullable=True),
        sa.Column("output_data", sa.JSON(), nullable=True),
        sa.Column("parameters", sa.JSON(), nullable=True),
        sa.Column("parameter_data", sa.JSON(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_packages_created_at"), "packages", ["created_at"], unique=False
    )
    op.create_index(op.f("ix_packages_name"), "packages", ["name"], unique=False)
    op.create_index(
        op.f("ix_packages_updated_at"), "packages", ["updated_at"], unique=False
    )
    op.create_table(
        "connections",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("project_id", sa.UUID(), nullable=True),
        sa.Column("source_package_id", sa.UUID(), nullable=True),
        sa.Column("target_package_id", sa.UUID(), nullable=True),
        sa.Column("source_handle", sa.String(), nullable=True),
        sa.Column("target_handle", sa.String(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.id"],
        ),
        sa.ForeignKeyConstraint(
            ["source_package_id"],
            ["packages.id"],
        ),
        sa.ForeignKeyConstraint(
            ["target_package_id"],
            ["packages.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_connections_created_at"), "connections", ["created_at"], unique=False
    )
    op.create_index(
        op.f("ix_connections_updated_at"), "connections", ["updated_at"], unique=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_connections_updated_at"), table_name="connections")
    op.drop_index(op.f("ix_connections_created_at"), table_name="connections")
    op.drop_table("connections")
    op.drop_index(op.f("ix_packages_updated_at"), table_name="packages")
    op.drop_index(op.f("ix_packages_name"), table_name="packages")
    op.drop_index(op.f("ix_packages_created_at"), table_name="packages")
    op.drop_table("packages")
    op.drop_index(op.f("ix_projects_updated_at"), table_name="projects")
    op.drop_index(op.f("ix_projects_name"), table_name="projects")
    op.drop_index(op.f("ix_projects_created_at"), table_name="projects")
    op.drop_table("projects")
    op.drop_index(op.f("ix_api_tokens_updated_at"), table_name="api_tokens")
    op.drop_index(op.f("ix_api_tokens_token"), table_name="api_tokens")
    op.drop_index(op.f("ix_api_tokens_created_at"), table_name="api_tokens")
    op.drop_table("api_tokens")
    op.drop_index(op.f("ix_user_references_updated_at"), table_name="user_references")
    op.drop_index(op.f("ix_user_references_google_id"), table_name="user_references")
    op.drop_index(op.f("ix_user_references_email"), table_name="user_references")
    op.drop_index(op.f("ix_user_references_created_at"), table_name="user_references")
    op.drop_table("user_references")
    op.drop_index(
        op.f("ix_organization_references_updated_at"),
        table_name="organization_references",
    )
    op.drop_index(
        op.f("ix_organization_references_name"), table_name="organization_references"
    )
    op.drop_index(
        op.f("ix_organization_references_created_at"),
        table_name="organization_references",
    )
    op.drop_table("organization_references")
    # ### end Alembic commands ###
