"""Added student_id to Student model

Revision ID: 7a568134b97e
Revises: 195034536082
Create Date: 2023-11-19 19:47:40.563516

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7a568134b97e'
down_revision = '195034536082'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('grade', schema=None) as batch_op:
        batch_op.alter_column('student_id',
               existing_type=mysql.VARCHAR(length=20),
               type_=sa.String(length=10),
               existing_nullable=False)
        batch_op.alter_column('course_code',
               existing_type=mysql.VARCHAR(length=20),
               type_=sa.String(length=10),
               existing_nullable=False)
        batch_op.alter_column('grade',
               existing_type=mysql.VARCHAR(length=5),
               type_=sa.String(length=2),
               existing_nullable=False)
        batch_op.alter_column('created_at',
               existing_type=mysql.DATETIME(),
               nullable=False)
        batch_op.alter_column('updated_at',
               existing_type=mysql.DATETIME(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('grade', schema=None) as batch_op:
        batch_op.alter_column('updated_at',
               existing_type=mysql.DATETIME(),
               nullable=True)
        batch_op.alter_column('created_at',
               existing_type=mysql.DATETIME(),
               nullable=True)
        batch_op.alter_column('grade',
               existing_type=sa.String(length=2),
               type_=mysql.VARCHAR(length=5),
               existing_nullable=False)
        batch_op.alter_column('course_code',
               existing_type=sa.String(length=10),
               type_=mysql.VARCHAR(length=20),
               existing_nullable=False)
        batch_op.alter_column('student_id',
               existing_type=sa.String(length=10),
               type_=mysql.VARCHAR(length=20),
               existing_nullable=False)

    # ### end Alembic commands ###