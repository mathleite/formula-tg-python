from typing import Dict

from src.race.car.abstract_race_car import AbstractRaceCar
from src.race.car.exceptions.unsupported_car_types import UnsupportedCarTypes
from src.race.car.muscle_car import MuscleCar
from src.race.car.sportive_car import SportiveCar


class CarFactory:
    _supported_car_types: Dict[str, AbstractRaceCar] = {
        "muscle": MuscleCar(),
        "sportive": SportiveCar(),
    }

    def __init__(self, car_type: str) -> None:
        _car_type_in_lower: str = car_type.lower()
        self._check_car_type(_car_type_in_lower)
        self._entity: AbstractRaceCar = self._supported_car_types[_car_type_in_lower]

    def create(self) -> AbstractRaceCar:
        return self._entity

    def _check_car_type(self, car_type: str) -> None:
        if car_type not in self._supported_car_types:
            raise UnsupportedCarTypes()
