# test_jaccard_dist.py

import unittest
from src.divergences import jaccard_dist, jaccard_sim

class TestDivergences(unittest.TestCase):

    def test_jaccard_sim(self):
        route_standard = ["Rome", "Milan", "Verona"]
        route_actual = ["Rome", "Milan", "Bergamo"]
        jaccard_similarity = jaccard_sim(set(route_standard), set(route_actual))
        self.assertEqual(jaccard_similarity, 0.5)

    def test_jaccard_dist(self):
        route_standard = ["Rome", "Milan", "Verona"]
        route_actual = ["Rome", "Milan", "Bergamo"]
        jaccard_distance = jaccard_dist(set(route_standard), set(route_actual))
        self.assertEqual(jaccard_distance, 0.5)

if __name__ == '__main__':
    unittest.main()