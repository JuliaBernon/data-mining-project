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
    print(intersection)
    print(union)
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




# Tests
all_cities = ["Rome", "Milan", "Verona", "Venezia", "Bergamo", "Bolzano", "Trento"]
route_standard = ["Rome", "Milan", "Verona"]
route_actual = ["Rome", "Milan", "Bergamo"]


# Test for jaccard_dist
jaccard_similarity = jaccard_sim(set(route_standard), set(route_actual))
print("Jaccard similarity : ", jaccard_similarity)