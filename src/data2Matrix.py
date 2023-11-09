### This file contains a function to transform a route into a matrix ###

import json

# read and parse cities.json
with open("./data/cities.json", "r") as cities_file:
    cities = json.load(cities_file)
# cities = ["Trento", "Roma", "Venizia"]

# read and parse merchTypes.json
with open("./data/merchTypes.json", "r") as merchTypes_file:
    merchandise_types = json.load(merchTypes_file)


def pairs_of_cities(cities):
    '''
    Return a list of pairs of cities
    cities : List[str]
    '''
    pairs = []
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            pairs.append((cities[i], cities[j]))
    return pairs


def route_to_matrix(route):
    '''
    Return a matrix of a given route, with the number of merchandise transported
    route : List[Dict[str, Any]]
    '''
    pairs_from_route = []
    merch_types_from_route = []
    
    for step in route:
        pair = (step["from"], step["to"])
        pairs_from_route.append(pair)
        for merch_type in step["merchandise"]:
            merch_types_from_route.append(merch_type)

    pairs_from_route = list(set(pairs_from_route))
    merch_types_from_route = list(set(merch_types_from_route))

    matrix = [[0 for i in range(len(merchandise_types))] for j in range(len(pairs_of_cities(cities)))]
    for step in route:
        for merch_type in step["merchandise"]:
            matrix[pairs_from_route.index((step["from"], step["to"]))][merch_types_from_route.index(merch_type)] = step["merchandise"][merch_type]

    return matrix





# # for tests

# with open("./data/standard.json", "r") as standard_file:
#     standard_routes = json.load(standard_file)

# routes = []
# for route in standard_routes:
#     routes.append(route["route"])

# pairs = pairs_of_cities(cities)
# merch_types = merchandise_types
# matrix = route_to_matrix(routes[0])

# print(matrix)
