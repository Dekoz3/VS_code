import sqlalchemy

from .users import users_table

metadata = sqlalchemy.MetaData()


posts_table = sqlalchemy.Table(
    "posts_table",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey(users_table.c.id)),
    sqlalchemy.Column("item", sqlalchemy.String(20)),
    sqlalchemy.Column("unit_of_measure", sqlalchemy.String(20)),
    sqlalchemy.Column("quantity", sqlalchemy.Integer()),
    sqlalchemy.Column("price_wo_vat", sqlalchemy.Integer()),
    sqlalchemy.Column("value_wo_vat", sqlalchemy.Integer()),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime()),
)