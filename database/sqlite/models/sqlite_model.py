from database.sqlite.sqlite import Sqlite

from peewee import Model


class SqliteModel(Model):
    class Meta:
        database = Sqlite().get_database()
