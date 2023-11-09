### This file contains different functions used to compute divergences between two routes ###

import math
from scipy.spatial import distance

## Using Euclidean distance between two routes
def euclidean_dist(route1, route2, elts):
    '''
    Compute the Euclidean distance between two routes given a set of cities or merchandise types
    route1 : List[Dict[str, Any]]
    route2 : List[Dict[str, Any]]
    elts : List[str]
    euclidean_dist(route1, route2, elts) -> float
    '''
    route1 = [1 if elt in route1 else 0 for elt in elts]
    route2 = [1 if elt in route2 else 0 for elt in elts]
    
    return distance.euclidean(route1, route2)

## Using the Jaccard Index
def jaccard_sim(set1, set2):
    '''
    Compute the Jaccard similarity between two sets
    set1 : Set[Any]
    set2 : Set[Any]
    jaccard_sim(set1, set2) -> float
    '''

    intersection = set1.intersection(set2)
    union = set1.union(set2)
    if len(union) == 0:
        return 0
    else:
        return len(intersection) / len(union)
    
def jaccard_dist(set1, set2):
    '''
    Compute the Jaccard distance between two sets : the lower the distance, the more divergence
    set1 : Set[Any]
    set2 : Set[Any]
    jaccard_dist(set1, set2) -> float
    '''
    return 1 - jaccard_sim(set1, set2)

## Using Cosine distance
def cosine_dist(set1, set2, elts):
    '''
    Compute the cosine distance between two sets
    set1 : Set[Any]
    set2 : Set[Any]
    cosine_dist(set1, set2) -> float
    '''
    set1 = [1 if elt in set1 else 0 for elt in elts]
    set2 = [1 if elt in set2 else 0 for elt in elts]

    return distance.cosine(set1, set2)

# Using Hamming distance
def hamming_dist(route1, route2, elts):
    '''
    '''

    
    return distance.hamming(route1, route2)

# Using Levenshtein distance

## Innovative divergences :






# # tests

# cities = ["Rome", "Milan", "Verona", "Bergamo", "Venice"]
# # route_standard = ["Rome", "Milan", "Verona"]
# # route_actual = ["Rome", "Milan", "Bergamo"]
# # # e : 1.4142135623730951, j : 0.5, c : 0.33333333333333326

# # route_standard = ["Rome", "Milan", "Verona"]
# # route_actual = ["Rome", "Milan", "Bergamo", "Venice"]
# # # e : 1.7320508075688772, j : 0.6, c : 0.42264973081037416

# # route_standard = ["Rome", "Milan", "Verona"]
# # route_actual = ["Rome", "Milan", "Verona"]
# # # e : 0, j : 0, c : 0

# # route_standard = ["Rome", "Milan", "Verona"]
# # route_actual = ["Rome", "Milan", "Verona", "Bergamo"]
# # # e : 1, j : 0.25, c : 0.1339745962155614

# # route_standard = ["Rome", "Milan", "Verona"]
# # route_actual = ["Bergamo", "Venice"]
# # # e : 2.23606797749979, j : 1, c : 1

# route_standard = ["Rome", "Milan", "Verona"]
# route_actual = ["Bergamo", "Venice", "Verona"]
# # e : 2, j : 0.8, c : 0.6666666666666666

# print("eucl dist : ", euclidean_dist(route_standard, route_actual, cities))
# print("jaccard dist : ", jaccard_dist(set(route_standard), set(route_actual)))
# print("cos dist : ", cosine_dist(set(route_standard), set(route_actual), cities))