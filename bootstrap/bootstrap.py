from app.race.car.models.car_model import CarModel
from app.race.events.models.event_model import EventModel
from app.race.models.race_model import RaceModel
from app.race.driver.models.driver_model import DriverModel
from database.sqlite.sqlite import Sqlite


class Bootstrap:
    @staticmethod
    def setup() -> None:
        database = Sqlite()

        if not database.connect():
            raise Exception('Database not connected!')

        database.get_database().create_tables([
            DriverModel,
            CarModel,
            RaceModel,
            EventModel,
        ])
