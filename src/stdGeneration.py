### This file is used to generate data for standard routes ###
# run : python3 src/stdGeneration.py <number_of_routes>

import json
import sys
import dataGenerator.stdGenerator

## getting the list of cities, merchandise types and drivers

# read and parse cities.json
with open("./data/cities.json", "r") as cities_file:
    cities = json.load(cities_file)

# read and parse merchTypes.json
with open("./data/merchTypes.json", "r") as merchTypes_file:
    merchandise_types = json.load(merchTypes_file)


## generate standard.json
def generate_standard_routes(nb_std_routes):
    '''
    Returns a list of standard routes.

    Parameters:
    nb_std_routes (int): The number of standard routes to generate.

    Returns:
    list: A list of dictionaries representing the standard routes. Each dictionary contains the "id" and "route" keys.
    '''
    standard_routes = []
    for i in range(nb_std_routes):
        standard_routes.append({
            "id": f"s{i + 1}",
            "route": dataGenerator.stdGenerator.generate_route(cities, merchandise_types)
        })
    return standard_routes

if len(sys.argv) > 1:
    nb_std_routes = int(sys.argv[1])
    standard_routes = generate_standard_routes(nb_std_routes)
else: # default values if none given
    nb_std_routes = 500
    standard_routes = generate_standard_routes(500)

# save data into standard.json
if __name__ == "__main__":
    with open(f"./data/standard.json", "w") as standard_file:
        json.dump(standard_routes, standard_file, indent=4)

print(f"stdGeneration.py executed successfully : {len(standard_routes)} routes generated in ./data/standard.json")
# run with default values : python3 ./src/stdGeneration.py 500