### This file is used to print all the data in a readable format ###

import json
# from src.divergences import euclidean_dist, cosine_dist, jaccard_dist

# Read and parse standard routes
with open("./data/standard.json", "r") as standard_file:
    standard_routes = json.load(standard_file)

# Read and parse actual routes
with open("./data/actual.json", "r") as actual_file:
    actual_routes = json.load(actual_file)

# Read and parse drivers
with open("./data/drivers.json", "r") as drivers_file:
    drivers = json.load(drivers_file)

# Read and parse cities
with open("./data/cities.json", "r") as cities_file:
    cities = json.load(cities_file)

# Read and parse merchTypes
with open("./data/merchTypes.json", "r") as merchTypes_file:
    merchTypes = json.load(merchTypes_file)

## Print data

# # print standard routes
# print("Standard routes :")
# for route in standard_routes:
#     print(f"Route {route['id']}:")
#     for step in route["route"]:
#         print(f"\tFrom {step['from']} to {step['to']} with {step['merchandise']}")
#     print("\n")


# # print actual routes
# print("Actual routes :")
# for route in actual_routes:
#     print(f"Route {route['id']} (driver {route['driver']}) associated to standard route {route['sroute']}:")
#     for step in route["route"]:
#         print(f"\tFrom {step['from']} to {step['to']} with {step['merchandise']}")
#     print("\n")

# ## Print, for each standard route, the associated actual routes
# print("Standard routes and associated actual routes :")
# for route in standard_routes:
#     print(f"Standard route {route['id']} :")
#     for actual_route in actual_routes:
#         if actual_route["sroute"] == route["id"]:
#             print(f"\tActual route {actual_route['id']} (driver {actual_route['driver']})")
#     print("\n")

# ## Print, for each driver, the associated standard routes and actual routes
# print("Drivers and associated actual routes :")
# for driver in drivers:
#     print(f"Driver {driver} :")
#     for route in standard_routes:
#         if route["id"] in [actual_route["sroute"] for actual_route in actual_routes if actual_route["driver"] == driver]:
#             print(f"\t{route['id']} : {[actual_route['id'] for actual_route in actual_routes if actual_route['sroute'] == route['id'] and actual_route['driver'] == driver]}")
#     print("\n")

# # Print, for each standard route, the associated actual routes and the divergences between them
# for standard_route in standard_routes:
#     print(f"Standard route {standard_route['id']} :")
#     standard_route_set = set()
#     for step in standard_route["route"]:
#         standard_route_set.update(step["from"], step["to"])
    
#     for actual_route in actual_routes:
#         if actual_route["sroute"] == standard_route["id"]:
#             actual_route_set = set()
#             for step in actual_route["route"]:
#                 actual_route_set.update(step["from"], step["to"])
            
#             euclidean_distance = euclidean_dist(standard_route_set, actual_route_set, cities)
#             jaccard_distance = jaccard_dist(standard_route_set, actual_route_set)
#             cosine_distance = cosine_dist(standard_route_set, actual_route_set, cities)
#             print(f"\tActual route {actual_route['id']} (driver {actual_route['driver']})")
#             print(f"\t\tDivergences: e_dist = {euclidean_distance}, j_dist = {jaccard_distance}, c_dist = {cosine_distance}")
#     print("\n")

# # For standard_route in standard_routes, print the id of the driver who did it
# for standard_route in standard_routes:
#     for actual_route in actual_routes:
#         if actual_route["sroute"] == standard_route["id"]:
#             print(f"Standard route {standard_route['id']} done by driver {actual_route['driver']}")
#     print("\n")

# Then, for each driver, print the id of the standard and actual routes he did
for driver in drivers:
    print(f"Driver {driver['id']} :")
    for actual_route in actual_routes:
        if actual_route["driver"] == driver["id"]:
            print(f"\tActual route {actual_route['id']} (standard route {actual_route['sroute']})")
    print("\n")



