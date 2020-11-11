from abc import ABC, abstractmethod
from src.race.car.abstract_car_entity import AbstractCarEntity


class AbstractCarEntityBuilder(ABC):
    @abstractmethod
    def build_color(self, color: str) -> None:
        pass

    @abstractmethod
    def build_position(self, position: str) -> None:
        pass

    @abstractmethod
    def build_brand(self, brand: str) -> None:
        pass

    @abstractmethod
    def get_entity(self) -> AbstractCarEntity:
        pass
