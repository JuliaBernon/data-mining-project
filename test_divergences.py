# divergences__test.py

import unittest
from src import divergences

class TestDivergences(unittest.TestCase):
    def test_euclidean_dist(self):
        all_cities = ["Rome", "Milan", "Verona", "Venezia", "Bergamo", "Bolzano", "Trento"]
        route_standard = ["Rome", "Milan", "Verona"]
        route_actual = ["Rome", "Milan", "Bergamo"]
        euclidean_distance = divergences.euclidean_dist(route_standard, route_actual, all_cities)
        self.assertEqual(euclidean_distance, 1.4142135623730951)

    def test_jaccard_sim(self):
        route_standard = ["Rome", "Milan", "Verona"]
        route_actual = ["Rome", "Milan", "Bergamo"]
        jaccard_similarity = divergences.jaccard_sim(set(route_standard), set(route_actual))
        self.assertEqual(jaccard_similarity, 0.5)

    def test_jaccard_dist(self):
        route_standard = ["Rome", "Milan", "Verona"]
        route_actual = ["Rome", "Milan", "Bergamo"]
        jaccard_distance = divergences.jaccard_dist(set(route_standard), set(route_actual))
        self.assertEqual(jaccard_distance, 0.5)

if __name__ == '__main__':
    unittest.main()