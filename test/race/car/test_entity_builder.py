import unittest
from unittest_data_provider import data_provider
from src.race.car.car_entity_builder import CarEntityBuilder
from src.race.car.car_entity import CarEntity


class TestEntityBuilder(unittest.TestCase):
    _provideEntityAttributesToBuild = lambda: [
        ['red', '1', 'Mclaren'],
        ['blue', '2', 'Ferrari'],
        ['black', '20', 'Bugatti'],
    ]

    @data_provider(_provideEntityAttributesToBuild)
    def test__entity_builder__should_build(self, color, position, brand):
        builder = CarEntityBuilder()
        builder.build_color(color)
        builder.build_position(position)
        builder.build_brand(brand)

        entity_result = builder.get_entity()

        self.assertEqual(color, entity_result.color)
        self.assertEqual(position, entity_result.position)
        self.assertEqual(brand, entity_result.brand)


if __name__ == '__main__':
    unittest.main()
