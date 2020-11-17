from abc import ABC, abstractmethod


class AbstractRaceCar(ABC):
    @abstractmethod
    def position(self) -> str:
        pass

    @abstractmethod
    def type(self) -> str:
        pass

    @staticmethod
    @abstractmethod
    def make():
        pass
