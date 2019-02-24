"""initial install

Revision ID: ed0adee82f59
Revises: 
Create Date: 2019-02-23 20:05:13.298984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed0adee82f59'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ticket',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ticket', sa.String(length=10), nullable=True),
    sa.Column('sponsor', sa.String(length=10), nullable=True),
    sa.Column('status', sa.String(length=15), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ticket_ticket'), 'ticket', ['ticket'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userid', sa.String(length=64), nullable=True),
    sa.Column('fullname', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_userid'), 'user', ['userid'], unique=True)
    op.create_table('worklog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('workdate', sa.DateTime(), nullable=True),
    sa.Column('hours', sa.Float(), nullable=True),
    sa.Column('message', sa.String(length=100), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('ticket_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ticket_id'], ['ticket.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_worklog_workdate'), 'worklog', ['workdate'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_worklog_workdate'), table_name='worklog')
    op.drop_table('worklog')
    op.drop_index(op.f('ix_user_userid'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_ticket_ticket'), table_name='ticket')
    op.drop_table('ticket')
    # ### end Alembic commands ###