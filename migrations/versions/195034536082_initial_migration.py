"""Initial migration

Revision ID: 195034536082
Revises: 
Create Date: 2023-11-17 13:41:50.221473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '195034536082'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('course',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('course_code', sa.String(length=20), nullable=False),
    sa.Column('course_name', sa.String(length=80), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('course_code')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.String(length=20), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=False),
    sa.Column('last_name', sa.String(length=80), nullable=False),
    sa.Column('major', sa.String(length=80), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('student_id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('role', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('grade',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.String(length=20), nullable=False),
    sa.Column('course_code', sa.String(length=20), nullable=False),
    sa.Column('grade', sa.String(length=5), nullable=False),
    sa.Column('semester', sa.String(length=20), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['course_code'], ['course.course_code'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.student_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('grade')
    op.drop_table('user')
    op.drop_table('student')
    op.drop_table('course')
    # ### end Alembic commands ###
