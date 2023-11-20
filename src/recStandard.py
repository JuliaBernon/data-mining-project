# in actual.json, identify every couple of cities that compose each route

import json
import pandas as pd
import random
import dataGenerator.newStdGenerator

with open("./data/actual.json") as actual_file:
    actual_routes = json.load(actual_file)

with open("./data/merchTypes.json","r") as merchTypes_file:
    merchandise_types = json.load(merchTypes_file)

# function to transform a route into a list of pairs of cities
def route_to_pairs(route):
    '''
    Returns a list of pairs of cities from a route.
    route : list(dict(str, str))
    '''
    pairs = []
    for i in range(len(route)):
        pairs.append((route[i]["from"], route[i]["to"]))
    return pairs

# store the pairs of cities of each actual route in a list
pairs_in_actual_routes = []
for route in actual_routes:
    pairs_in_actual_routes.append(route_to_pairs(route["route"]))
print(pairs_in_actual_routes)

# create a function that returns the number of a pair of cities in the list of lists of pairs
def number_of_pair(pair, pairs):
    '''
    Returns the number of a pair of cities in the list of lists of pairs.
    pair : tuple(str, str)
    pairs : list(list(tuple(str, str)))
    '''
    count = 0
    for route in pairs:
        if pair in route:
            count += 1
    return count

for pair_actual in pairs_in_actual_routes:
    pair_number = {}

    # iterate over each pair in pairs_in_actual_routes and update the number in pair_number
    for pair_actual in pairs_in_actual_routes:
        for pair in pair_actual:
            if pair in pair_number:
                pair_number[pair] += 1
            else:
                pair_number[pair] = 1
            
# create a function that computes the frequency of each pair
def compute_pair_frequency(pair, pairs):
    '''
    Computes the frequency of a pair based on the formula: frequency_of_a_pair = number_of_pair / total_number_of_pairs.
    pair : tuple(str, str)
    pairs : list(list(tuple(str, str)))
    '''
    total_pairs = sum(len(route) for route in pairs)
    pair_count = number_of_pair(pair, pairs)
    frequency = pair_count / total_pairs
    return frequency

# compute the frequency of each pair
most_frequent_pairs = []
for pair in sorted(pair_number, key=pair_number.get, reverse=True):
    frequency = compute_pair_frequency(pair, pairs_in_actual_routes)
    print(pair, " : ", frequency)
    if frequency > 0.0075:
        most_frequent_pairs.append(pair)
# print(most_frequent_pairs)

# generate recStandard.json
nb_recstd_routes = 100 # define the number of standard routes
recstd_routes = []
for i in range(nb_recstd_routes):
    recstd_routes.append({
        "id": f"r{i + 1}",
        "route": dataGenerator.newStdGenerator.generate_new_route(most_frequent_pairs, merchandise_types)
    })

# save data into recStandard.json
with open("./data/recStandard.json", "w") as recstd_file:
    json.dump(recstd_routes, recstd_file, indent=4)
