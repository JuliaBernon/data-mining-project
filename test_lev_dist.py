# FILEPATH: /C:/Users/julia/Documents/GitHub/data-mining-project/test_lev_distance.py

import unittest
from src.lev_distance import levenshtein_distance_list

class TestLevenshteinDistance(unittest.TestCase):

    def test_levenshtein_distance1(self):
        l1 = ["apple", "banana", "cherry"]
        l2 = ["apple", "banana", "cherry"]
        self.assertEqual(levenshtein_distance_list(l1, l2), 0)

    def test_levenshtein_distance2(self):
        l1 = ["apple", "banana", "cherry"]
        l2 = ["apple", "banana", "pear"]
        self.assertEqual(levenshtein_distance_list(l1, l2), 1)

    def test_levenshtein_distance3(self):
        l1 = ["apple", "banana", "cherry"]
        l2 = ["apple", "pear", "cherry"]
        self.assertEqual(levenshtein_distance_list(l1, l2), 1)

    def test_levenshtein_distance4(self):
        l1 = ["apple", "banana", "cherry"]
        l2 = ["pear", "banana", "cherry"]
        self.assertEqual(levenshtein_distance_list(l1, l2), 1)

    def test_levenshtein_distance5(self):
        l1 = ["apple", "banana", "cherry"]
        l2 = ["pear", "orange", "grape"]
        self.assertEqual(levenshtein_distance_list(l1, l2), 3)

if __name__ == '__main__':
    unittest.main()