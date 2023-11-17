# FILEPATH: /c:/Users/julia/Documents/GitHub/data-mining-project/test_recStandard.py

import unittest
from src.recStandard import route_to_pairs, frequency_of_pair

class TestRecStandard(unittest.TestCase):

    def test_route_to_pairs(self):
        route = [{"from": "Rome", "to": "Milan"}, {"from": "Milan", "to": "Verona"}]
        expected_pairs = [("Rome", "Milan"), ("Milan", "Verona")]
        self.assertEqual(route_to_pairs(route), expected_pairs)

    def test_frequency_of_pair(self):
        pairs = [[("Rome", "Milan"), ("Milan", "Verona")], [("Rome", "Milan"), ("Milan", "Bergamo")]]
        pair = ("Rome", "Milan")
        expected_frequency = 2
        self.assertEqual(frequency_of_pair(pair, pairs), expected_frequency)

        pair = ("Milan", "Verona")
        expected_frequency = 1
        self.assertEqual(frequency_of_pair(pair, pairs), expected_frequency)

        pair = ("Rome", "Verona")
        expected_frequency = 0
        self.assertEqual(frequency_of_pair(pair, pairs), expected_frequency)

if __name__ == '__main__':
    unittest.main()