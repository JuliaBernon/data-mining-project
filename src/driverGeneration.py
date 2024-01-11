### This file creates drivers.json according to drivers' agenda ###

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

# Adapt drivers to main rules
def adapt_driver(driver, main_rules):
    """
    Adapt the driver's preferences based on the main rules.

    Args:
        driver (dict): The driver's information.
        main_rules (dict): The main rules for preference adaptation.

    Returns:
        None
    """
    proba_main_rules = main_rules["proba_main_rules"]
    for city in main_rules["best_cities"]:
        if random.random() < proba_main_rules:
            driver["pref_cities"][city] = 0.9
    for city in main_rules["worst_cities"]:
        if random.random() < proba_main_rules:
            driver["pref_cities"][city] = 0.1
    for merch in main_rules["best_merchs"]:
        if random.random() < proba_main_rules:
            driver["pref_merch"][merch] = 0.9
    for merch in main_rules["worst_merchs"]:
        if random.random() < proba_main_rules:
            driver["pref_merch"][merch] = 0.1
    for assoc_rule in main_rules["assoc_rules"]:
        if random.random() < proba_main_rules:
            driver["assoc_rules"].append(assoc_rule)

# generate drivers.json
def generate_drivers(nb_drivers, main_rules):
    '''
    Returns a list of drivers.

    Parameters:
    nb_drivers (int): The number of drivers to generate.
    main_rules (dict): The main rules to apply to the driver's agenda.

    Returns:
    list: A list of drivers, each represented as a dictionary with keys "id" and "agenda".
    '''
    drivers = []
    for i in range(nb_drivers):
        driver_agenda = generate_driver(cities, merchandise_types)
        if main_rules != {}:
            adapt_driver(driver_agenda, main_rules)
        drivers.append({"id": f"d{i + 1}", "agenda": driver_agenda})
    return drivers

if len(sys.argv) > 1:
    nb_drivers = int(sys.argv[1])
    drivers = generate_drivers(nb_drivers,main_rules)
else: # default values if none given
    drivers = generate_drivers(10,main_rules)

# run with default values : python3 ./src/driverGeneration.py 10

# save data into drivers.json
if __name__ == "__main__":
    with open("./data/drivers.json", "w") as drivers_file:
        json.dump(drivers, drivers_file, indent=4)

print(f"driverGeneration done : {len(drivers)} drivers generated in ./data/drivers.json")