"""Adding in models for certificate sources

Revision ID: 1ff763f5b80b
Revises: 4dc5ddd111b8
Create Date: 2015-08-01 15:24:20.412725

"""

# revision identifiers, used by Alembic.
revision = '1ff763f5b80b'
down_revision = '4dc5ddd111b8'

from alembic import op
import sqlalchemy as sa

import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sources',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(length=32), nullable=True),
    sa.Column('options', sqlalchemy_utils.types.json.JSONType(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('plugin_name', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('certificate_source_associations',
    sa.Column('source_id', sa.Integer(), nullable=True),
    sa.Column('certificate_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['certificate_id'], ['certificates.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['source_id'], ['destinations.id'], ondelete='cascade')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('certificate_source_associations')
    op.drop_table('sources')
    ### end Alembic commands ###
