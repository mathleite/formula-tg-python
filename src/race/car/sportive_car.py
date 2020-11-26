from typing import Optional

from src.race.car.abstract_race_car import AbstractRaceCar


class SportiveCar(AbstractRaceCar):
    def __init__(self) -> None:
        self._position = None
        self._type = 'sportive'

    @property
    def position(self) -> Optional[str]:
        return self._position

    @position.setter
    def position(self, value) -> None:
        self._position = value

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value) -> None:
        self._type = value

    @staticmethod
    def make():
        return SportiveCar()
