import random
import json
from dataGenerator.actualGenerator import generate_actual_route


# read and parse cities.json
with open("./data/cities.json", "r") as cities_file:
    cities = json.load(cities_file)

# read and parse merchTypes.json
with open("./data/merchTypes.json", "r") as merchTypes_file:
    merchandise_types = json.load(merchTypes_file)

#get the standard routes
with open("./data/standard.json", "r") as standard_file:
    standard_routes = json.load(standard_file)
    nb_std_routes = len(standard_routes)

# read and parse drivers.json
with open("./data/drivers.json", "r") as drivers_file:
    drivers = json.load(drivers_file)

## generate actual.json
nb_act_routes = 1 # define the number of actual routes 
actual_routes = []
for i in range(nb_act_routes):
    std_route_number = random.randint(0, nb_std_routes-1)
    actual_routes.append({
        "id": f"a{i + 1}",
        "driver": random.choice(drivers),
        "sroute": f"{standard_routes[std_route_number]['id']}",
        "route": generate_actual_route(standard_routes[std_route_number]["route"], cities, merchandise_types)
    })

# save data into actual.json
with open("./data/actual.json", "w") as actual_file:
    json.dump(actual_routes, actual_file, indent=4)

