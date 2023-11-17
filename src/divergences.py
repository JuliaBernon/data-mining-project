### This file contains different functions used to compute distances between two routes ###

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
def hamming_dist(set1, set2):
    '''
    Compute the Hamming distance between two sets of cities
    set1 : List[str]
    set2 : List[str]
    hamming_dist(route1, route2) -> float
    '''
    if len(set1)!=len(set2):
        raise ValueError("Hamming distance is not defined for sequences of unequal length")

    return distance.hamming(set1, set2)

# Using Levenshtein distance


# def lev_distance_modified(route1, route2):
#     '''
#     Compute a distance based on Levenshtein distance between two routes
#     route1 : List[Dict[str, Any]]
#     route2 : List[Dict[str, Any]]
#     lev_distance_modified(route1, route2) -> float
#     '''


# def levenshtein_distance(s, t):
#     m = len(s)
#     n = len(t)
#     d = [[0] * (n + 1) for i in range(m + 1)]  

#     for i in range(1, m + 1):
#         d[i][0] = i

#     for j in range(1, n + 1):
#         d[0][j] = j
    
#     for j in range(1, n + 1):
#         for i in range(1, m + 1):
#             if s[i - 1] == t[j - 1]:
#                 cost = 0
#             else:
#                 cost = 1
#             d[i][j] = min(d[i - 1][j] + 1,      # deletion
#                           d[i][j - 1] + 1,      # insertion
#                           d[i - 1][j - 1] + cost) # substitution   

#     return d[m][n]

## Innovative divergences :






# # tests

# cities = ["Rome", "Milan", "Verona", "Bergamo", "Venice"]
# # route_standard = ["Rome", "Milan", "Verona"]
# # route_actual = ["Rome", "Milan", "Bergamo"]
# # # e : 1.4142135623730951, j : 0.5, c : 0.33333333333333326, h : 0.3333333333333333

# # route_standard = ["Rome", "Milan", "Verona"]
# # route_actual = ["Rome", "Milan", "Bergamo", "Venice"]
# # # e : 1.7320508075688772, j : 0.6, c : 0.42264973081037416

# # route_standard = ["Rome", "Milan", "Verona"]
# # route_actual = ["Rome", "Milan", "Verona"]
# # # e : 0, j : 0, c : 0, h : 0

# # route_standard = ["Rome", "Milan", "Verona"]
# # route_actual = ["Rome", "Milan", "Verona", "Bergamo"]
# # # e : 1, j : 0.25, c : 0.1339745962155614, h : 

# # route_standard = ["Rome", "Milan", "Verona"]
# # route_actual = ["Bergamo", "Venice"]
# # # e : 2.23606797749979, j : 1, c : 1, h : 

# # route_standard = ["Rome", "Milan", "Verona"]
# # route_actual = ["Bergamo", "Venice", "Verona"]
# # e : 2, j : 0.8, c : 0.6666666666666666, h : 0.6666666666666666

# print("eucl dist : ", euclidean_dist(route_standard, route_actual, cities))
# print("jaccard dist : ", jaccard_dist(set(route_standard), set(route_actual)))
# print("cos dist : ", cosine_dist(set(route_standard), set(route_actual), cities))
# print("hamming dist : ", hamming_dist(route_standard, route_actual))