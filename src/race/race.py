from typing import Optional

from src.race.abstract_race import AbstractRace
from src.race.car.cars_collection import CarsCollection
from src.race.car.exceptions.race_not_started_types import RaceNotStarted


class Race(AbstractRace):
    def __init__(self, cars: CarsCollection) -> None:
        self._cars: CarsCollection = cars
        self._winners: Optional[CarsCollection] = None
        self._is_race_start: bool = False
        self._is_race_over: bool = False

    def start(self) -> None:
        if self._is_race_over and not self._is_race_start:
            raise RaceNotStarted()

        self._is_race_start = True

    def end(self) -> None:
        if not self._is_race_start:
            raise RaceNotStarted()

        self._is_race_over = True
        self._winners = self._cars

    def retrieve_first_three_winners(self) -> list:
        if self._winners and len(self._winners):
            return self._winners[:3]

        raise RaceNotStarted()
