### This file is used to generate data for standard and actual routes ###

import json
import random
import routeGenerator

## getting the list of cities, merchandise types and drivers

# read and parse cities.json
with open("./data/cities.json", "r") as cities_file:
    cities = json.load(cities_file)

# read and parse merchTypes.json
with open("./data/merchTypes.json", "r") as merchTypes_file:
    merchandise_types = json.load(merchTypes_file)

# read and parse drivers.json
with open("./data/drivers.json", "r") as drivers_file:
    drivers = json.load(drivers_file)


## generate standard.json
nb_std_routes = 100 # define the number of standard routes
standard_routes = []
for i in range(nb_std_routes):
    standard_routes.append({
        "id": f"s{i + 1}",
        "route": routeGenerator.generate_route(cities, merchandise_types)
    })

# save data into standard.json
with open("./data/standard.json", "w") as standard_file:
    json.dump(standard_routes, standard_file, indent=4)

## generate actual.json
nb_act_routes = 500 # define the number of actual routes 
actual_routes = []
for i in range(nb_act_routes):
    actual_routes.append({
        "id": f"a{i + 1}",
        "driver": random.choice(drivers),
        "sroute": f"s{random.randint(1, nb_std_routes)}",
        "route": routeGenerator.generate_route(cities, merchandise_types)
    })

# save data into actual.json
with open("./data/actual.json", "w") as actual_file:
    json.dump(actual_routes, actual_file, indent=4)


# create a variation in the number of visited cities, of visited cities, of merchandise types, of merchandise quantities
# create an actual route based on a standard route, with a probability that gives which variations we apply



