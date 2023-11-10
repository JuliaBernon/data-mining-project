### This file creates drivers.json according to drivers' agenda ###

import json
from dataGenerator.driverGenerator import generate_driver

# read and parse cities.json
with open("./data/cities.json", "r") as cities_file:
    cities = json.load(cities_file)

# read and parse merchTypes.json
with open("./data/merchTypes.json", "r") as merchTypes_file:
    merchandise_types = json.load(merchTypes_file)

## generate drivers.json
nb_drivers = 20 # define the number of drivers
drivers = []
for i in range(nb_drivers):
    drivers.append({"id": f"d{i + 1}", "agenda": generate_driver(cities, merchandise_types)})

# save data into drivers.json
with open("./data/drivers.json", "w") as drivers_file:
    json.dump(drivers, drivers_file, indent=4)