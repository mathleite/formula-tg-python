from typing import Optional

from abc import ABC, abstractmethod


class AbstractRaceCar(ABC):
    @abstractmethod
    def position(self) -> Optional[str]:
        pass

    @abstractmethod
    def type(self) -> str:
        pass

    @staticmethod
    @abstractmethod
    def make():
        pass

    def __str__(self):
        return f'Type: {self.type}, Position: {self.position}'
