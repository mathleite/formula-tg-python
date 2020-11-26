from abc import ABC, abstractmethod


class AbstractRace(ABC):
    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def end(self) -> None:
        pass

    @abstractmethod
    def retrieve_first_three_winners(self) -> list:
        pass
