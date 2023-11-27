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

#get the standard routes
with open("./results/recStandard.json", "r") as rec_standard_file:
    rec_standard_routes = json.load(rec_standard_file)
nb_std_routes = len(rec_standard_routes)

# read and parse drivers.json
with open("./data/drivers.json", "r") as drivers_file:
    drivers = json.load(drivers_file)

## generate actual.json
def generate_actual_routes(number_of_routes):
    '''
    Returns a list of actual routes.
    number_of_routes : int
    '''
    actual_routes = []
    for i in range(number_of_routes):
        std_route_number = random.randint(0, nb_std_routes-1)
        driver = random.choice(drivers)
        actual_routes.append({
            "id": f"a{i + 1}",
            "driver": driver["id"],
            "sroute": f"{rec_standard_routes[std_route_number]['id']}",
            "route": generate_actual_route(rec_standard_routes[std_route_number]["route"], cities, merchandise_types, driver)
        })
    return actual_routes

if len(sys.argv) > 1:
    nb_act_routes = int(sys.argv[1])
    actual_routes = generate_actual_routes(nb_act_routes)
else:
    actual_routes = generate_actual_routes(1000)


# save data into actual.json
if __name__ == "__main__":
    with open("./results/newActual.json", "w") as actual_file:
        json.dump(actual_routes, actual_file, indent=4)
