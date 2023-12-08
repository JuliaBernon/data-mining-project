### This file creates drivers.json according to drivers' agenda ###
# run : python3 src/mainRulesGeneration.py nb_best_cities,nb_worst_cities,nb_best_roads,nb_worst_roads,nb_best_merch,nb_worst_merch,nb_assoc_rules

import json
import sys
import random

# read and parse cities.json
with open("./data/cities.json", "r") as cities_file:
    cities = json.load(cities_file)

# read and parse merchTypes.json
with open("./data/merchTypes.json", "r") as merchTypes_file:
    merchandise_types = json.load(merchTypes_file)

def generate_main_rules(nb_best_cities,nb_worst_cities,nb_best_roads,nb_worst_roads,nb_best_merch,nb_worst_merch,nb_assoc_rules,proba_main_rules):
    main_rules = {}
    main_rules["proba_main_rules"] = proba_main_rules
    main_rules["best_cities"] = random.sample(cities,nb_best_cities)
    cities_left = []
    for city in cities :
        if city not in main_rules["best_cities"]:
            cities_left.append(city)
    main_rules["worst_cities"] = random.sample(cities_left,min(nb_worst_cities,len(cities_left)))
    main_rules["best_roads"] = []
    for i in range(nb_best_roads):
        main_rules["best_roads"].append(random.sample(cities,2))
    main_rules["worst_roads"] = []
    for i in range(nb_worst_roads):
        main_rules["worst_roads"].append(random.sample(cities,2))
    main_rules["best_merchs"] = random.sample(merchandise_types,nb_best_merch)
    merch_left = []
    for merch in merchandise_types :
        if merch not in main_rules["best_merchs"]:
            merch_left.append(merch)
    main_rules["worst_merchs"] = random.sample(merch_left,min(nb_worst_merch,len(merch_left)))
    main_rules["assoc_rules"] = [random.sample(merchandise_types,2) for i in range(nb_assoc_rules)]
    return main_rules

if len(sys.argv) > 7:
    main_rules = generate_main_rules(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8])
else:
    main_rules = generate_main_rules(1,1,3,3,1,1,2,1)

# save data into drivers.json
if __name__ == "__main__":
    with open("./data/mainRules.json", "w") as main_rules_file:
        json.dump(main_rules, main_rules_file, indent=4)

print("mainRulesGeneration done")