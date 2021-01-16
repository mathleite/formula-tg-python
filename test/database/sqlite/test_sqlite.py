from unittest import TestCase

from peewee import SqliteDatabase

from database.sqlite.sqlite import Sqlite


class TestSqlite(TestCase):
    def test__sqlite_instance__should_connect(self) -> None:
        self.assertTrue(Sqlite().connect())

    def test__sqlite_get_database__should_be_sqlite_database_instance(self) -> None:
        self.assertTrue(
            isinstance(
                Sqlite().get_database(), SqliteDatabase
            )
        )
