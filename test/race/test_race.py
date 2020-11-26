from unittest import TestCase

from src.race.abstract_race import AbstractRace
from src.race.car.cars_collection import CarsCollection
from src.race.car.exceptions.race_not_started_types import RaceNotStarted
from src.race.race import Race
from src.race.car.service.car_builder_by_amount import CarBuilderByAmount


class TestRace(TestCase):
    def test__retrieved_first_three_race_winners__should_retrieve_the_first_three_winners(self) -> None:
        fake_car_list: CarsCollection = CarBuilderByAmount.build(10)

        race_instance: AbstractRace = Race(fake_car_list)
        race_instance.start()
        race_instance.end()

        expected_car_list: list = fake_car_list[:3]
        retrieved_three_winners: list = race_instance.retrieve_first_three_winners()

        self.assertEqual(expected_car_list, retrieved_three_winners)
        self.assertEqual(len(expected_car_list), len(retrieved_three_winners))

    def test__race_not_start_exception__should_raise_exception_when_end_race_without_start(self) -> None:
        with self.assertRaises(RaceNotStarted):
            fake_car_list: CarsCollection = CarBuilderByAmount.build(10)
            race_instance: AbstractRace = Race(fake_car_list)
            race_instance.end()

    def test__race_not_start_exception__should_raise_exception_when_retrieve_winners_without_start_race(self) -> None:
        with self.assertRaises(RaceNotStarted):
            fake_car_list: CarsCollection = CarBuilderByAmount.build(10)
            race_instance: AbstractRace = Race(fake_car_list)
            race_instance.retrieve_first_three_winners()
