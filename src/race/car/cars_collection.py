from src.race.car.abstract_race_car import AbstractRaceCar


class CarsCollection:
    def __init__(self, cars: list):
        self._cars = cars
        self._list_index: int = 0

    def __len__(self):
        return len(self._cars)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result: AbstractRaceCar = self._cars[self._list_index]
        except IndexError:
            raise StopIteration

        self._list_index += 1
        return result

    def __getitem__(self, item):
        return self._cars[item]
