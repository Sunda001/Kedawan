"""Idk what is this lmfao

Revision ID: f19c4ff9a3de
Revises: f2ef997605e5
Create Date: 2023-05-21 01:23:52.713123

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f19c4ff9a3de'
down_revision = 'f2ef997605e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('visitor',
    sa.Column('id', mysql.INTEGER(unsigned=True), autoincrement=True, nullable=False),
    sa.Column('fast_links_id', mysql.INTEGER(unsigned=True), nullable=False),
    sa.Column('country_code', sa.String(length=2), nullable=False),
    sa.Column('visit_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['fast_links_id'], ['fast_links.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('fast_links', schema=None) as batch_op:
        batch_op.alter_column('visitor',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fast_links', schema=None) as batch_op:
        batch_op.alter_column('visitor',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)

    op.drop_table('visitor')
    # ### end Alembic commands ###
