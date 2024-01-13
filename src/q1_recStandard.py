### Generate a new standard route, given a set of pairs of cities and merchandise types ###

import json
import pandas as pd
import dataGenerator.newStdGenerator
import sys

from freqCities import most_frequent_pairs
import re

### Read and parse data ###

with open("./data/merchTypes.json","r") as merchTypes_file:
    merchandise_types = json.load(merchTypes_file)

### Generating a new route ###

# generate recStandard.json
def generate_recStandard(nb_routes, FI_file):
    '''
    Generate a new standard route, given a set of pairs of cities and merchandise types

    Args:
        nb_routes (int): The number of routes to generate
        FI_file (str): The file path of the frequency items file

    Returns:
        List[Dict[str, Any]]: A list of dictionaries representing the generated routes, each containing an "id" and "route" key

    Example:
        generate_recStandard(5, "/path/to/freq_items.csv")
    '''
    # pairs_of_cities = [(city1, city2), (city3, city4), ...]
    # merchandise_types = ['[item1]', '[item3, item4, ...]', ...]

    # analyse the most frequent merchandise types and itemsets based on freq_items.csv
    freq_items = pd.read_csv(FI_file)
    freq_items["itemsets"] = freq_items["itemsets"].apply(lambda x: re.findall(r'{.*?}', str(x))[0])
    cleaned_freq_items = [item.replace("'", "").replace("{","[").replace("}","]") for item in freq_items["itemsets"].values.tolist()]

    # find the most frequent pairs of cities in actual_routes based on freqCities.py
    most_freq_pairs = most_frequent_pairs(0.005)

    recstd_routes = []
    for i in range(nb_routes):
        recstd_routes.append({
            "id": f"s{i + 1}",
            "route": dataGenerator.newStdGenerator.generate_new_route(most_freq_pairs, cleaned_freq_items)
        })
    return recstd_routes

if len(sys.argv) > 1:
    nb_routes = int(sys.argv[1])
    FI_file = sys.argv[2]
    filename_to_save = sys.argv[3]
    recstd_routes = generate_recStandard(nb_routes, FI_file)
else: # default values if none given
    recstd_routes = generate_recStandard(500, "./data/csv/freq_items.csv")
    filename_to_save = "./results/recStandard.json"

# save data into recStandard.json
if __name__ == "__main__":
    with open(filename_to_save, "w") as recstd_file:
        json.dump(recstd_routes, recstd_file, indent=4)

# run with default values : python3 ./src/recStandard.py 500 ./data/csv/freq_items.csv ./results/recStandard.json
print(f"recStandard.py executed successfully : {len(recstd_routes)} routes generated in {filename_to_save}")