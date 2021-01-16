from os import getenv
from typing import Optional
from peewee import SqliteDatabase


class Sqlite:
    def __init__(self) -> None:
        self.database: SqliteDatabase = SqliteDatabase(
            f"{self._sanitize_environment_text(getenv('DATABASE_NAME'))}.db"
        )

    def get_database(self) -> SqliteDatabase:
        return self.database

    def connect(self) -> bool:
        return self.database.connect()

    @staticmethod
    def _sanitize_environment_text(text: Optional[str]) -> Optional[str]:
        return text.replace("\"", "") if text else None
