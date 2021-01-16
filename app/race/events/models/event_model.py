from peewee import DateTimeField, IntegerField, ForeignKeyField

from app.race.car.models.car_model import CarModel
from app.race.models.race_model import RaceModel
from app.utils.date import Date
from database.sqlite.models.sqlite_model import SqliteModel


class EventModel(SqliteModel):
    race_id: ForeignKeyField = ForeignKeyField(RaceModel, backref='event')
    car_id: ForeignKeyField = ForeignKeyField(CarModel, backref='race')
    current_position: IntegerField = IntegerField()
    last_position: IntegerField = IntegerField()
    created_at: DateTimeField = DateTimeField(default=Date.get_current_datetime())
