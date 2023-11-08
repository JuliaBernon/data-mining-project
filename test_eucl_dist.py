# test_eucl_dist.py

import unittest
from src.divergences import euclidean_dist

class TestDivergences(unittest.TestCase):

    cities = ["Rome", "Milan", "Verona", "Bergamo", "Venice"]
    
    def test_euclidean_dist1(self):
        route_standard = ["Rome", "Milan", "Verona"]
        route_actual = ["Rome", "Milan", "Bergamo"]
        euclidean_distance = euclidean_dist(route_standard, route_actual, self.cities)
        self.assertEqual(euclidean_distance, 1.4142135623730951)

    def test_euclidean_dist2(self):
        route_standard = ["Rome", "Milan", "Verona"]
        route_actual = ["Rome", "Milan", "Bergamo", "Venice"]
        euclidean_distance = euclidean_dist(route_standard, route_actual, self.cities)
        self.assertEqual(euclidean_distance, 1.7320508075688772)

    def test_euclidean_dist3(self):
        route_standard = ["Rome", "Milan", "Verona"]
        route_actual = ["Rome", "Milan", "Verona"]
        euclidean_distance = euclidean_dist(route_standard, route_actual, self.cities)
        self.assertEqual(euclidean_distance, 0)

    def test_euclidean_dist4(self):
        route_standard = ["Rome", "Milan", "Verona"]
        route_actual = ["Rome", "Milan", "Verona", "Bergamo"]
        euclidean_distance = euclidean_dist(route_standard, route_actual, self.cities)
        self.assertEqual(euclidean_distance, 1)

    def test_euclidean_dist5(self):
        route_standard = ["Rome", "Milan", "Verona"]
        route_actual = ["Bergamo", "Venice"]
        euclidean_distance = euclidean_dist(route_standard, route_actual, self.cities)
        self.assertEqual(euclidean_distance, 2.23606797749979)

    def test_euclidean_dist6(self):
        route_standard = ["Rome", "Milan", "Verona"]
        route_actual = ["Bergamo", "Venice", "Verona"]
        euclidean_distance = euclidean_dist(route_standard, route_actual, self.cities)
        self.assertEqual(euclidean_distance, 2)

if __name__ == '__main__':
    unittest.main()

