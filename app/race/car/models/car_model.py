from peewee import CharField, DateTimeField, IntegerField, ForeignKeyField

from app.race.driver.models.driver_model import DriverModel
from app.utils.date import Date
from database.sqlite.models.sqlite_model import SqliteModel


class CarModel(SqliteModel):
    brand: CharField = CharField()
    number: IntegerField = CharField()
    driver_id: ForeignKeyField = ForeignKeyField(DriverModel, backref='car', unique=True)
    created_at: DateTimeField = DateTimeField(default=Date.get_current_datetime())
