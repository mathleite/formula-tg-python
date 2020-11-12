from src.race.car.abstract_race_car import AbstractRaceCar


class SportiveCar(AbstractRaceCar):
    def __init__(self) -> None:
        self._position = ''
        self._type = ''

    @property
    def position(self) -> str:
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
