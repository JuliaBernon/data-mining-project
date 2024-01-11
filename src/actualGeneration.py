### This file is used to generate the actual.json file. ###

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

# read and parse drivers.json
with open("./data/drivers.json", "r") as drivers_file:
    drivers = json.load(drivers_file)

## generate actual.json
def generate_actual_routes(number_of_routes, std_routes_file):
    '''
    Returns a list of actual routes.

    Parameters:
    number_of_routes (int): The number of actual routes to generate.
    std_routes_file (file): The file containing the standard routes.

    Returns:
    list: A list of dictionaries representing the actual routes.
    '''
    actual_routes = []
    standard_routes = json.load(std_routes_file) # load standard routes to be used
    nb_std_routes = len(standard_routes)
    for i in range(number_of_routes):
        std_route_number = random.randint(0, nb_std_routes-1)
        driver = random.choice(drivers)
        actual_routes.append({
            "id": f"a{i + 1}", # actual route id
            "driver": driver["id"], # corresponding driver id
            "sroute": f"{standard_routes[std_route_number]['id']}", # corresponding standard route id
            "route": generate_actual_route(standard_routes[std_route_number]["route"], cities, merchandise_types, driver) # actual route
        })
    return actual_routes

# print(generate_actual_routes(100, open("./data/standard.json", "r")))

if len(sys.argv) >= 4:
    nb_act_routes = int(sys.argv[1])
    std_routes_file = open(sys.argv[2], "r")
    filename_to_save = sys.argv[3]
    actual_routes = generate_actual_routes(nb_act_routes, std_routes_file)
else: # default values if none given
    filename_to_save = "./data/actual.json"
    actual_routes = generate_actual_routes(1000, "./data/standard500.json")

# run with default values : python3 ./src/actualGeneration.py 1000 ./data/standard500.json ./data/actual.json

# save data into actual.json
if __name__ == "__main__":
    with open(filename_to_save, "w") as actual_file:
        json.dump(actual_routes, actual_file, indent=4)

print(f"actualGeneration.py executed successfully : {len(actual_routes)} actual routes generated in {filename_to_save}")
