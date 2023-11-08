# test_jaccard_dist.py

import unittest
from src.divergences import jaccard_dist, jaccard_sim

class TestDivergences(unittest.TestCase):

    cities = ["Rome", "Milan", "Verona", "Bergamo", "Venice"]

    def test_jaccard_dist1(self):
        route_standard = ["Rome", "Milan", "Verona"]
        route_actual = ["Rome", "Milan", "Bergamo"]
        jaccard_distance = jaccard_dist(set(route_standard), set(route_actual))
        self.assertEqual(jaccard_distance, 0.5)

    def test_jaccard_dist2(self):
        route_standard = ["Rome", "Milan", "Verona"]
        route_actual = ["Rome", "Milan", "Bergamo", "Venice"]
        jaccard_distance = jaccard_dist(set(route_standard), set(route_actual))
        self.assertEqual(jaccard_distance, 0.6)
    
    def test_jaccard_dist3(self):
        route_standard = ["Rome", "Milan", "Verona"]
        route_actual = ["Rome", "Milan", "Verona"]
        jaccard_distance = jaccard_dist(set(route_standard), set(route_actual))
        self.assertEqual(jaccard_distance, 0.0)
    
    def test_jaccard_dist4(self):
        route_standard = ["Rome", "Milan", "Verona"]
        route_actual = ["Rome", "Milan", "Verona", "Bergamo"]
        jaccard_distance = jaccard_dist(set(route_standard), set(route_actual))
        self.assertEqual(jaccard_distance, 0.25)
    
    def test_jaccard_dist5(self):
        route_standard = ["Rome", "Milan", "Verona"]
        route_actual = ["Bergamo", "Venice"]
        jaccard_distance = jaccard_dist(set(route_standard), set(route_actual))
        self.assertEqual(jaccard_distance, 1.0)
    
    def test_jaccard_dist6(self):
        route_standard = ["Rome", "Milan", "Verona"]
        route_actual = ["Bergamo", "Venice", "Verona"]
        jaccard_distance = jaccard_dist(set(route_standard), set(route_actual))
        self.assertEqual(jaccard_distance, 0.8)

if __name__ == '__main__':
    unittest.main()