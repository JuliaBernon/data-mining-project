import random
import json
from dataGenerator.actualGenerator import generate_actual_route

with open("./data/standard.json", "r") as standard_file:
    standard_routes = json.load(standard_file)

# read and parse drivers.json
with open("./data/drivers.json", "r") as drivers_file:
    drivers = json.load(drivers_file)

#get the number of std routes
#TODO
nb_std_routes = 10

#extraction des routes 
#TODO
liste_std_routes = []

## generate actual.json
nb_act_routes = 500 # define the number of actual routes 
actual_routes = []
for i in range(nb_act_routes):
    std_route_number = random.randint(1, nb_std_routes)
    actual_routes.append({
        "id": f"a{i + 1}",
        "driver": random.choice(drivers),
        "sroute": f"s{std_route_number}",
        "route": generate_actual_route(liste_std_routes(std_route_number))
    })

# save data into actual.json
with open("./data/actual.json", "w") as actual_file:
    json.dump(actual_routes, actual_file, indent=4)

