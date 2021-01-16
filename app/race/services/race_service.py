from app.race.car.models.car_model import CarModel
from app.race.models.race_model import RaceModel


class RaceService:
    @staticmethod
    def check_conditions_to_start_race() -> bool:
        cars_length_to_start = 2

        if len(CarModel.select()) < cars_length_to_start:
            print("Race doesn't have enough cars!")
            return False

        if len(RaceModel.select()) == 0:
            print("Race doesn't exist!")
            return False

        return True
