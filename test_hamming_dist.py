# test_hamming_dist.py

import unittest
from src.divergences import hamming_dist

class TestDivergences(unittest.TestCase):

        def test_hamming_dist(self):
            route_standard = ["Rome", "Milan", "Verona"]
            route_actual = ["Rome", "Milan", "Bergamo"]
            hamming_distance = hamming_dist(route_standard, route_actual)
            self.assertEqual(hamming_distance, 0.3333333333333333)

        def test_hamming_dist3(self):
            route_standard = ["Rome", "Milan", "Verona"]
            route_actual = ["Rome", "Milan", "Verona"]
            hamming_distance = hamming_dist(route_standard, route_actual)
            self.assertEqual(hamming_distance, 0.0)

if __name__ == '__main__':
    unittest.main()