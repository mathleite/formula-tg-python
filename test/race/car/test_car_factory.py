import unittest
from unittest_data_provider import data_provider

from src.race.car.abstract_race_car import AbstractRaceCar
from src.race.car.car_factory import CarFactory
from src.race.car.exceptions.unsupported_car_types import UnsupportedCarTypes


class TestCarFactory(unittest.TestCase):
    _provideSupportedCarTypes = lambda: [
        ['muscle'],
        ['Muscle'],
        ['MUSCLE'],
        ['sportive'],
        ['Sportive'],
        ['SPORTIVE'],
    ]

    _provideUnsupportedCarTypes = lambda: [
        ['normal'],
        ['truck'],
        ['animal'],
        ['1223!@#'],
        ['muscle_'],
        ['sportive_'],
        ['sp0rt1v3'],
        ['mu2cl3'],
    ]

    @data_provider(_provideSupportedCarTypes)
    def test__should_create_car(self, car_type: str):
        factory: CarFactory = CarFactory()
        self.assertEqual(True, isinstance(factory.create(car_type), AbstractRaceCar))

    @data_provider(_provideUnsupportedCarTypes)
    def test__should_raise_unsupported_car_types_exception__when_given_unsupported_types(self, car_type: str):
        with self.assertRaises(UnsupportedCarTypes):
            factory: CarFactory = CarFactory()
            factory.create(car_type)


if __name__ == '__main__':
    unittest.main()
