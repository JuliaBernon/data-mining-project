### This file is used to generate the actual.json file. ###
# run : python3 src/actualGeneration.py <number_of_routes>

import random
import json
import sys
from dataGenerator.actualGenerator import generate_actual_route


# read and parse cities.json
with open("./data/cities.json", "r") as cities_file:
    cities = json.load(cities_file)

# read and parse merchTypes.json
with open("./data/merchTypes.json", "r") as merchTypes_file:
    merchandise_types = json.load(merchTypes_file)

# #get the standard routes
# with open("./data/standard.json", "r") as standard_file:
#     standard_routes = json.load(standard_file)
#     nb_std_routes = len(standard_routes)

# read and parse drivers.json
with open("./data/drivers.json", "r") as drivers_file:
    drivers = json.load(drivers_file)

## generate actual.json
def generate_actual_routes(number_of_routes, std_routes_file):
    '''
    Returns a list of actual routes.
    number_of_routes : int
    '''
    actual_routes = []
    standard_routes = json.load(std_routes_file)
    nb_std_routes = len(standard_routes)
    for i in range(number_of_routes):
        std_route_number = random.randint(0, nb_std_routes-1)
        driver = random.choice(drivers)
        actual_routes.append({
            "id": f"a{i + 1}",
            "driver": driver["id"],
            "sroute": f"{standard_routes[std_route_number]['id']}",
            "route": generate_actual_route(standard_routes[std_route_number]["route"], cities, merchandise_types, driver)
        })
    return actual_routes

# print(generate_actual_routes(100, open("./data/standard.json", "r")))

if len(sys.argv) >= 4:
    nb_act_routes = int(sys.argv[1])
    std_routes_file = open(sys.argv[2], "r")
    filename_to_save = sys.argv[3]
    actual_routes = generate_actual_routes(nb_act_routes, std_routes_file)
else:
    actual_routes = generate_actual_routes(1000, "./data/standard.json")
    filename_to_save = "./data/actual.json"


# save data into actual.json
if __name__ == "__main__":
    with open(filename_to_save, "w") as actual_file:
        json.dump(actual_routes, actual_file, indent=4)


