from src.race.car.abstract_car_entity import AbstractCarEntity


class CarEntity(AbstractCarEntity):
    def __init__(self):
        self._color = ''
        self._position = ''
        self._brand = ''

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value) -> None:
        self._color = value

    @property
    def position(self) -> str:
        return self._position

    @position.setter
    def position(self, value) -> None:
        self._position = value

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, value) -> None:
        self._brand = value
