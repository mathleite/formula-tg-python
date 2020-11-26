from src.race.car.cars_collection import CarsCollection
from src.race.car.car_factory import CarFactory


class CarBuilderByAmount:
    @staticmethod
    def build(amount: int) -> CarsCollection:
        cars: list = []
        for index in range(amount):
            factory: CarFactory = CarFactory()
            cars.append(
                factory.create(
                    'muscle' if ((index % 2) == 0) else 'sportive'
                )
            )

        return CarsCollection(cars)
