# test_cosine_dist.py

import unittest
from src.divergences import cosine_dist

class TestDivergences(unittest.TestCase):
        
        cities = ["Rome", "Milan", "Verona", "Bergamo", "Venice"]
        
        # with two routes of same length
        def test_cosine_dist(self):
            route_standard = ["Rome", "Milan", "Verona"]
            route_actual = ["Rome", "Milan", "Bergamo"]
            cosine_distance = cosine_dist(set(route_standard), set(route_actual), self.cities)
            self.assertEqual(cosine_distance, 0.33333333333333326)

        # with two routes of different length
        def test_cosine_dist2(self):
            route_standard = ["Rome", "Milan", "Verona"]
            route_actual = ["Rome", "Milan", "Bergamo", "Venice"]
            cosine_distance = cosine_dist(set(route_standard), set(route_actual), self.cities)
            self.assertEqual(cosine_distance, 0.42264973081037416)

        # with two routes of same length and same cities
        def test_cosine_dist3(self):
            route_standard = ["Rome", "Milan", "Verona"]
            route_actual = ["Rome", "Milan", "Verona"]
            cosine_distance = cosine_dist(set(route_standard), set(route_actual), self.cities)
            self.assertEqual(cosine_distance, 0.0)

        # with two routes of different length and different cities
        def test_cosine_dist4(self):
            route_standard = ["Rome", "Milan", "Verona"]
            route_actual = ["Bergamo", "Venice"]
            cosine_distance = cosine_dist(set(route_standard), set(route_actual), self.cities)
            self.assertEqual(cosine_distance, 1.0)

        # with two routes of different length and same cities
        def test_cosine_dist5(self):
            route_standard = ["Rome", "Milan", "Verona"]
            route_actual = ["Rome", "Milan", "Verona", "Bergamo"]
            cosine_distance = cosine_dist(set(route_standard), set(route_actual), self.cities)
            self.assertEqual(cosine_distance, 0.1339745962155614)

        # with two routes of same length and different cities  
        def test_cosine_dist6(self):
            route_standard = ["Rome", "Milan", "Verona"]
            route_actual = ["Bergamo", "Venice", "Verona"]
            cosine_distance = cosine_dist(set(route_standard), set(route_actual), self.cities)
            self.assertEqual(cosine_distance, 0.6666666666666666)

if __name__ == '__main__':
    unittest.main()