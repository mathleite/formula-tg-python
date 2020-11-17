from typing import Callable, Dict

from src.race.car.abstract_race_car import AbstractRaceCar
from src.race.car.exceptions.unsupported_car_types import UnsupportedCarTypes
from src.race.car.muscle_car import MuscleCar
from src.race.car.sportive_car import SportiveCar


class CarFactory:
    _supported_car_types: Dict[str, Callable[[], AbstractRaceCar]] = {
        "muscle": MuscleCar.make,
        "sportive": SportiveCar.make,
    }

    def create(self, car_type: str) -> AbstractRaceCar:
        _car_type_in_lower: str = car_type.lower()
        self._check_car_type(_car_type_in_lower)
        return self._supported_car_types[_car_type_in_lower]()

    def _check_car_type(self, car_type: str) -> None:
        if car_type not in self._supported_car_types:
            raise UnsupportedCarTypes()
