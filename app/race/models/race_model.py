from peewee import CharField, DateTimeField, IntegerField

from app.utils.date import Date
from database.sqlite.models.sqlite_model import SqliteModel


class RaceModel(SqliteModel):
    name: CharField = CharField()
    type: CharField = CharField()
    laps: IntegerField = IntegerField()
    created_at: DateTimeField = DateTimeField(default=Date.get_current_datetime())
    started_at: DateTimeField = DateTimeField(null=True, default=None)
    finished_at: DateTimeField = DateTimeField(null=True, default=None)
