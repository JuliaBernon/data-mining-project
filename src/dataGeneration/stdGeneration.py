### This file is used to generate data for standard routes ###

import json
import random
import dataGenerator.routeGenerator

## getting the list of cities, merchandise types and drivers

# read and parse cities.json
with open("./data/cities.json", "r") as cities_file:
    cities = json.load(cities_file)

# read and parse merchTypes.json
with open("./data/merchTypes.json", "r") as merchTypes_file:
    merchandise_types = json.load(merchTypes_file)


## generate standard.json
nb_std_routes = 100 # define the number of standard routes
standard_routes = []
for i in range(nb_std_routes):
    standard_routes.append({
        "id": f"s{i + 1}",
        "route": dataGenerator.routeGenerator.generate_route(cities, merchandise_types)
    })

# save data into standard.json
with open("./data/standard.json", "w") as standard_file:
    json.dump(standard_routes, standard_file, indent=4)

