## This file contains functions to analyze the different routes a driver has taken ##

import json
import pandas as pd
import matplotlib.pyplot as plt

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
# from mlxtend.frequent_patterns import fpgrowth
from merchFIAndAssoRules import route_to_list_merch
#from freqCities import most_frequent_pairs
import re
import dataGenerator.newStdGenerator
import time as t

def get_drivers(actual_routes):
    '''
    Returns a list of all the drivers in actual_routes.
    actual_routes : list(dict(str, str))
    '''
    drivers = []
    for route in actual_routes:
        if route["driver"] not in drivers:
            drivers.append(route["driver"])
    return drivers

def get_routes_per_driver(actual_routes, driver):
    '''
    Returns a list of all the routes done by a given driver.
    actual_routes : list(dict(str, str))
    driver : str
    '''
    routes_per_driver = []
    for route in actual_routes:
        if route["driver"] == driver:
            routes_per_driver.append(route)
    return routes_per_driver

# create a function to get the FIs and ARs for a given driver
def FIandAssoRulesForOneDriver(support, threshold, actual_routes, driver):
    start = t.time()
    actualRoutesDriver = get_routes_per_driver(actual_routes,driver)
    print(t.time()-start)
    all_routes = []
    for i in range(len(actualRoutesDriver)):
        all_routes.append(route_to_list_merch(actualRoutesDriver[i]["route"]))
    print(t.time()-start)
    for route in all_routes:
        if route ==  []:
            all_routes.remove(route)
    print(t.time()-start)
    all_routes = [[item for sublist in route for item in sublist] if isinstance(route[0], list) else route for route in all_routes]
    print(t.time()-start)
    te = TransactionEncoder()
    te_ary = te.fit(all_routes).transform(all_routes)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    print(t.time()-start)
    frequent_itemsets = apriori(df, min_support=support, use_colnames=True, max_len=3)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=threshold)
    print(t.time()-start)
    return frequent_itemsets, rules

def generate_recStandardForOneDriver(nb_routes, freq_items):
    '''
    Generate a new standard route, given a set of pairs of cities and merchandise types

    pairs_of_cities : List[(str, str)]
    merchandise_types : List[List[str]]

    generate_new_route(pairs_of_cities, merchandise_types) -> List[Dict[str, Any]]
    '''
    # analyse the most frequent merchandise types and itemsets
    freq_items["itemsets"] = freq_items["itemsets"].apply(lambda x: re.findall(r'{.*?}', str(x))[0])
    cleaned_freq_items = [item.replace("'", "").replace("{","[").replace("}","]") for item in freq_items["itemsets"].values.tolist()]

    # find the most frequent pairs of cities in actual_routes based on freqCities.py
    #most_freq_pairs = most_frequent_pairs(0.005)
    most_freq_pairs = []
    recstd_routes = []
    for i in range(nb_routes):
        recstd_routes.append({
            "route": dataGenerator.newStdGenerator.generate_new_route(most_freq_pairs, cleaned_freq_items)
        })
    return recstd_routes

if __name__ == "__main__":
    # Read and parse standard routes
    with open("./data/standard.json", "r") as standard_file:
        standard_routes = json.load(standard_file)
    # Read and parse actual routes
    with open("./data/actual.json", "r") as actual_file:
        actual_routes = json.load(actual_file)
    drivers = get_drivers(actual_routes)
    drivers = [drivers[0]]
    for driver in drivers :
        frequent_itemsets, rules = FIandAssoRulesForOneDriver(0.4, 0.5, actual_routes, driver)
        #frequent_itemsets.to_csv("./data/csv/freq_items_driver1.csv", index=False)
        #rules.to_csv("./data/csv/asso_rules_driver1.csv", index=False)
        recstd_routes = generate_recStandardForOneDriver(1, frequent_itemsets)
        # save data
        frequent_itemsets.to_json("./data/freq_items_driver1.json", orient="records")
        with open(f"./data/recstd_{driver}.json", "w") as recstd_driver_file:
            json.dump(recstd_routes, recstd_driver_file)