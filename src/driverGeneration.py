### This file creates drivers.json according to drivers' agenda ###
# run : python3 src/driverGeneration.py <number_of_drivers>

import json
import sys
from dataGenerator.driverGenerator import generate_driver

# read and parse cities.json
with open("./data/cities.json", "r") as cities_file:
    cities = json.load(cities_file)

# read and parse merchTypes.json
with open("./data/merchTypes.json", "r") as merchTypes_file:
    merchandise_types = json.load(merchTypes_file)

## generate drivers.json
def generate_drivers(nb_drivers):
    '''
    Returns a list of drivers.
    nb_drivers : int
    '''
    drivers = []
    for i in range(nb_drivers):
        drivers.append({"id": f"d{i + 1}", "agenda": generate_driver(cities, merchandise_types)})
    return drivers

if len(sys.argv) > 1:
    nb_drivers = int(sys.argv[1])
    drivers = generate_drivers(nb_drivers)
else:
    drivers = generate_drivers(10)

# save data into drivers.json
if __name__ == "__main__":
    with open("./data/drivers.json", "w") as drivers_file:
        json.dump(drivers, drivers_file, indent=4)