from src.race.car.abstract_car_entity_builder import AbstractCarEntityBuilder
from src.race.car.car_entity import CarEntity


class CarEntityBuilder(AbstractCarEntityBuilder):
    def __init__(self):
        self._entity = CarEntity()

    def build_color(self, color: str) -> None:
        self._entity.color = color

    def build_position(self, position: str) -> None:
        self._entity.position = position

    def build_brand(self, brand: str) -> None:
        self._entity.brand = brand

    def get_entity(self) -> CarEntity:
        entity = self._entity
        return entity
