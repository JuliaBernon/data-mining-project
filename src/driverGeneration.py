### This file creates drivers.json according to drivers' agenda ###
# run : python3 src/driverGeneration.py <number_of_drivers>

import json
import sys
import random
from dataGenerator.driverGenerator import generate_driver

# read and parse cities.json
with open("./data/cities.json", "r") as cities_file:
    cities = json.load(cities_file)

# read and parse merchTypes.json
with open("./data/merchTypes.json", "r") as merchTypes_file:
    merchandise_types = json.load(merchTypes_file)

# read and parse mainRules.json
with open("./data/mainRules.json", "r") as mainRules_file:
    main_rules = json.load(mainRules_file)

#adapt drivers to main rules
def adapt_driver(driver,main_rules):
    proba_main_rules = main_rules["proba_main_rules"]
    for city in main_rules["best_cities"]:
        if random.random() < proba_main_rules :
            driver["pref_cities"][city] = 0.9
    for city in main_rules["worst_cities"]:
        if random.random() < proba_main_rules :
            driver["pref_cities"][city] = 0.1
    for merch in main_rules["best_merchs"]:
        if random.random() < proba_main_rules :
            driver["pref_merch"][merch] = 0.9
    for merch in main_rules["worst_merchs"]:
        if random.random() < proba_main_rules :
            driver["pref_merch"][merch] = 0.1
    for assoc_rule in main_rules["assoc_rules"]:
        if random.random() < proba_main_rules :
            driver["assoc_rules"].append(assoc_rule)

## generate drivers.json
def generate_drivers(nb_drivers,main_rules):
    '''
    Returns a list of drivers.
    nb_drivers : int
    '''
    drivers = []
    for i in range(nb_drivers):
        driver_agenda = generate_driver(cities, merchandise_types)
        if main_rules != {}:
            adapt_driver(driver_agenda,main_rules)
        drivers.append({"id": f"d{i + 1}", "agenda": driver_agenda})
    return drivers

if len(sys.argv) > 1:
    nb_drivers = int(sys.argv[1])
    drivers = generate_drivers(nb_drivers,main_rules)
else:
    drivers = generate_drivers(10,main_rules)

# save data into drivers.json
if __name__ == "__main__":
    with open("./data/drivers.json", "w") as drivers_file:
        json.dump(drivers, drivers_file, indent=4)