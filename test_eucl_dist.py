import unittest
from src.divergences import euclidean_dist

class TestDivergences(unittest.TestCase):
    
    def test_euclidean_dist(self):
        route_standard = ["Rome", "Milan", "Verona"]
        route_actual = ["Rome", "Milan", "Bergamo"]
        elts = ["Rome", "Milan", "Verona", "Bergamo"]
        euclidean_distance = euclidean_dist(route_standard, route_actual, elts)
        self.assertEqual(euclidean_distance, 1.4142135623730951)

if __name__ == '__main__':
    unittest.main()

