from abc import ABC, abstractmethod


class AbstractCarEntity(ABC):
    @abstractmethod
    def color(self) -> str:
        pass

    @abstractmethod
    def position(self) -> str:
        pass

    @abstractmethod
    def brand(self) -> str:
        pass
