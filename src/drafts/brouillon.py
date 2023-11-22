# given the set of standard routes that the company has now and the actual routes 
# that the drivers have done so far, it produces a recommendation to the company on 
# what standard routes it should have

import json
from scipy.spatial import distance
from data2Matrix import *
from math import *
# import numpy as np
from Levenshtein import distance as levenshtein_distance

with open("./data/actual.json") as actual_file:
    actual_routes = json.load(actual_file)

with open("./data/standard.json") as standard_file:
    standard_routes = json.load(standard_file)

routes_std = []
routes_act = []
for std_route in standard_routes:
    routes_std.append(std_route["route"])
for act_route in actual_routes:
    routes_act.append(act_route["route"])

# print(routes_std)
# print("\n")
# print(routes_act)
# print("\n")

pairs = pairs_of_cities(cities)
merch_types = merchandise_types

# transform the first route of the standard_routes into a matrix
print("Standard route - sparse matrix :")
matrix_std = route_to_matrix(routes_std[0])
print(matrix_sparse(matrix_std))
print("\n")
print("Actual route - sparse matrix :")
matrix_act = route_to_matrix(routes_act[0])
print(len(matrix_act[0]))
print("\n")
print(len(matrix_act))

# compute hamming distance between the two matrices
hamming_dist_vect = []
for i in range(len(matrix_std)):
    hamming_dist_vect.append(distance.hamming(matrix_std[i], matrix_act[i]))

for i in range(len(hamming_dist_vect)):
    if hamming_dist_vect[i] != 0:
        print("Hamming distance between lines ", i, " : ", hamming_dist_vect[i])
print("\n")

# using matrix norm
norm1 = 0
norm22 = 0
for i in range(len(matrix_std)):
    for j in range(len(matrix_std[i])):
        norm1 += abs(matrix_std[i][j] - matrix_act[i][j])
        norm22 += (matrix_std[i][j] - matrix_act[i][j])**2

norm_inf = max([abs(matrix_std[i][j] - matrix_act[i][j]) for i in range(len(matrix_std)) for j in range(len(matrix_std[i]))])

norm2 = sqrt(norm22)
print("N1(Std, Act): ", norm1)
print("N2(Std, Act) : ", norm2)
print("N_inf(Std, Act): ", norm_inf)     
print("\n")

# using levenshtein distance
for route_std in standard_routes:
    for route_act in actual_routes:
        print("Levenshtein distance between ", route_std["route"], " and ", route_act["route"], " : ", levenshtein_distance(route_std["route"], route_act["route"]))


## En fait, faudrait faire le calcul pour chaque route standard, entre la route standard et chacune des routes actuelles associées

## couples de villes les plus fréquents
## association rules with merchandises 
## clustering and frequent itemsets