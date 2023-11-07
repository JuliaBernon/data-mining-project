import json
import random

# for testing purposes
# nb_cities = len(cities)
# nb_merchandise_types = len(merchandise_types)

## Generate our data for actual and standard routes

# read and parse cities.json
with open("./data/cities.json", "r") as cities_file:
    cities = json.load(cities_file)

# read and parse merchTypes.json
with open("./data/merchTypes.json", "r") as merchTypes_file:
    merchandise_types = json.load(merchTypes_file)




