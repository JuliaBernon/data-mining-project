# in actual.json, identify every couple of cities that compose each route

import json
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

from mlxtend.preprocessing import TransactionEncoder

import pandas as pd
import json

with open("./data/actual.json") as actual_file:
    actual_routes = json.load(actual_file)

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

# create a function that returns the frequency of a pair of cities in the list of lists of pairs
def frequency_of_pair(pair, pairs):
    '''
    Returns the frequency of a pair of cities in the list of lists of pairs.
    pair : tuple(str, str)
    pairs : list(list(tuple(str, str)))
    '''
    count = 0
    for route in pairs:
        if pair in route:
            count += 1
    return count

for pair_actual in pairs_in_actual_routes:
    # for pair in pair_actual:
    #     print(pair, " : ", frequency_of_pair(pair, pairs_in_actual_routes))
    # print("\n")
    pair_number = {}

    # iterate over each pair in pairs_in_actual_routes and update the frequency in pair_number
    for pair_actual in pairs_in_actual_routes:
        for pair in pair_actual:
            if pair in pair_number:
                pair_number[pair] += 1
            else:
                pair_number[pair] = 1

# iterate over the dictionary and print each pair with its frequency, sorted by frequency
for pair in sorted(pair_number, key=pair_number.get, reverse=True):
    print(pair, " : ", pair_number[pair])

# function to transform a route into a list of merchandises for each step
def route_to_merchandises(route):
    '''
    Returns a list of merchandises for each step in a route.
    route : list(dict(str, str))
    '''
    merchandises = []
    for i in range(len(route)):
        merchandises.append(route[i]["merchandise"])
    return merchandises

def merchandise_types(merchandises):
    '''
    Returns the list of merchandise types in a list of merchandises.
    merchandises : list(dict(str, int))
    '''
    types = []
    for i in range(len(merchandises)):
        if merchandises[i] not in types:
            types.append(merchandises[i])
    return types

# select one route from actual.json
route = actual_routes[0]["route"]
print(route_to_merchandises(route))
print("\n")


def route_to_list_merch(route):
    '''
    Returns a list of dictionaries with the merchandise types for each step in a route.
    route : list(dict(str, str))
    '''
    route_merchandise_types = []
    for i, dictionary in enumerate(route_to_merchandises(route)):
        merchandise_types = list(dictionary.keys())

        route_merchandise_types.append(merchandise_types)
    return route_merchandise_types

# store the merchandise types of each actual route in a list
merchandise_types_in_actual_routes = []
for route in actual_routes:
    merchandise_types_in_actual_routes.append(route_to_list_merch(route["route"]))
print(merchandise_types_in_actual_routes)


##########



# Assuming merchandise_types_in_actual_routes is the list of routes

all_frequent_itemsets = []
all_association_rules = []

for route_merchandise_types in merchandise_types_in_actual_routes:
    # Convert the data format for Apriori
    te = TransactionEncoder()
    te_ary = te.fit(route_merchandise_types).transform(route_merchandise_types)
    df = pd.DataFrame(te_ary, columns=te.columns_)

    # Apply Apriori algorithm
    frequent_itemsets = apriori(df, min_support=0.5, use_colnames=True)

    # Generate association rules
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

    # Append results to the list
    all_frequent_itemsets.append(frequent_itemsets)
    all_association_rules.append(rules)

# Print the results for each route
# for i, route_frequent_itemsets in enumerate(all_frequent_itemsets):
#     print(f"Route {i + 1} - Frequent Itemsets:")
# print(route_frequent_itemsets)

# for i, route_association_rules in enumerate(all_association_rules):
#     print(f"Route {i + 1} - Association Rules:")
# print(route_association_rules)

