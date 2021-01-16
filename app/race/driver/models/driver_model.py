from peewee import CharField, DateTimeField

from database.sqlite.models.sqlite_model import SqliteModel
from app.utils.date import Date


class DriverModel(SqliteModel):
    name: CharField = CharField(unique=True)
    created_at: DateTimeField = DateTimeField(default=Date.get_current_datetime())
