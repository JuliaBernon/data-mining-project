# File code to create recStandard.json
# steps that should be good to follow :
# 1. we analyze the actual routes taken by the drivers, and we compute the difference between the actual routes and the standard routes
# 2. we identify the most common diversions
# 3. based on the most common diversions, we recommend new standard routes
# 4. we put data in recStandard.json

import json
import random
import math

# Read and parse standard routes
with open("./data/standard.json", "r") as standard_file:
    standard_routes = json.load(standard_file)

# Read and parse actual routes
with open("./data/actual.json", "r") as actual_file:
    actual_routes = json.load(actual_file)

## Step 1
divergences = {} # store the divergences between actual and standard routes
rec_standard_routes = [] # store the recommended new standard routes


# function calcultateDivergence to calculate the divergence between two routes
def calculateDivergence(actual_route, standard_route):
    std_cities = set([route["from"] for route in standard_route])
    actual_cities = set([route["from"] for route in actual_route])
    # calculate the divergence 
    # here, the divergence is simply the number of cities visited by the driver that are not in the standard route
    divergence = len(actual_cities - std_cities)
    return divergence


# calculate the divergences between one actual route and the associated standard route
for actual_route in actual_routes :
    driver = actual_route["driver"]
    actual_route_id = actual_route["id"]
    standard_route_id = actual_route["sroute"]
    actual_route_info = actual_route["route"] # contains : from, to, merchandise

    standard_route = [route for route in standard_routes if route["id"] == standard_route_id][0]["route"]
    
    # calculate the divergence 
    divergence = calculateDivergence(actual_route_info, standard_route)
    print("standard_route_id: ", standard_route_id, " from ", standard_route[0]["from"], " to ", standard_route[0]["to"])
    print("standard steps :", [route["from"] for route in standard_route])
    print("actual_route_id: ", actual_route_id)
    print("actual steps : ", [route["from"] for route in actual_route_info])
    print("divergence: ", divergence)
    print("\n")

# # save data into recStandard.json
# with open("./data/recStandard.json", "w") as rec_standard_file:
#     json.dump(rec_standard_routes, rec_standard_file, indent=4)