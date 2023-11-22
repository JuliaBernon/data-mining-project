### Merch analysis ###
### This file contains funcions and scripts to obtain the most frequent transported merchandises in the actual routes. ###

import json
import matplotlib.pyplot as plt

with open("./data/actual.json") as actual_file:
    actual_routes = json.load(actual_file)

def route_to_merchandises(route):
    merchandises = []
    for step in route:
        merchandises.append(step["merchandise"])
    return merchandises

def route_to_list_merch(route):
    route_merchandise_types = []
    for dictionary in route_to_merchandises(route):
        merchandise_types = list(dictionary.keys())
        route_merchandise_types.append(merchandise_types)
    return route_merchandise_types

all_merchandise_types = [merch for route in actual_routes for merch in route_to_list_merch(route["route"])]
flat_merchandise_types = [merch_type for sublist in all_merchandise_types for merch_type in sublist]

def merch_frequency(merchandises):
    merchandises_number = {}
    n = len(merchandises)
    for merch in merchandises:
        if merch in merchandises_number:
            merchandises_number[merch] += 1
        else:
            merchandises_number[merch] = 1
    for merch in merchandises_number:
        merchandises_number[merch] /= n
    return merchandises_number
        
merchandises_number = merch_frequency(flat_merchandise_types)
print(merchandises_number)

# plot the most frequent merchandises
plt.bar(range(len(merchandises_number)), list(merchandises_number.values()), align='center')
plt.xticks(range(len(merchandises_number)), list(merchandises_number.keys()))
plt.xticks(rotation=90)
plt.xlabel("Merchandise")
plt.ylabel("Frequency")
plt.title("Merchandise frequency")
plt.show()