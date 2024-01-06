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
def FIandAssoRulesForOneDriver(support, threshold, actualRoutesDriver, driver):
    all_routes = []
    for i in range(len(actualRoutesDriver)):
        all_routes.append(route_to_list_merch(actualRoutesDriver[i]["route"]))
    for route in all_routes:
        if route ==  []:
            all_routes.remove(route)
    all_routes = [[item for sublist in route for item in sublist] if isinstance(route[0], list) else route for route in all_routes]
    te = TransactionEncoder()
    te_ary = te.fit(all_routes).transform(all_routes)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    frequent_itemsets = apriori(df, min_support=support, use_colnames=True, max_len=3)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=threshold)
    return frequent_itemsets, rules

def city_frequency(routes):
    all_cities = {}
    tot = 0
    for route in routes :
        true_route = route["route"]
        for step in true_route[:-1]:
            tot += 1
            if step["from"] in all_cities.keys():
                all_cities[step["from"]] += 1
            else :
                all_cities[step["from"]] = 1
        if true_route != [] :
            tot += 1
            if true_route[-1]["to"] in all_cities.keys():
                all_cities[true_route[-1]["to"]] += 1
            else :
                all_cities[true_route[-1]["to"]] = 1
    freqs = {}
    for city in all_cities.keys():
        freqs[city] = all_cities[city]/tot
    return freqs

def fav_cities_driver(actualRoutesDriver, city_freq, mult):
    freqs_driver = city_frequency(actualRoutesDriver)
    fav_cities = []
    for city in freqs_driver.keys() :
        if freqs_driver[city] >= mult*city_freq[city]:
            fav_cities.append(city)
    return fav_cities

def pairs_from_favs(fav_cities):
    pairs = []
    """ for i in range(len(fav_cities)-1):
        for j in range(i+1,len(fav_cities)):
            pairs.append((fav_cities[i],fav_cities[j])) """
    for i in range(len(fav_cities)):
        for j in range(len(fav_cities)):
            if i != j :
                pairs.append((fav_cities[i],fav_cities[j]))
    return pairs

def freq_cities_driver(actualRoutesDriver,number = 4,threshold = None):
    all_cities = {}
    for route in actualRoutesDriver :
        true_route = route["route"]
        for step in true_route:
            if step["from"] in all_cities.keys():
                all_cities[step["from"]] += 1
            else :
                all_cities[step["from"]] = 1
            if step["to"] in all_cities.keys():
                all_cities[step["to"]] += 1
            else :
                all_cities[step["to"]] = 1
    order = print(sorted(all_cities, key = lambda tup: all_cities[tup], reverse= True))
    return order[:min(len(order),number)]

def freq_pairs_driver(actualRoutesDriver,threshold):
    all_cities = {}
    tot = 0
    for route in actualRoutesDriver :
        true_route = route["route"]
        for step in true_route:
            if (step["from"], step["to"]) in all_cities.keys():
                all_cities[(step["from"],step["to"])] += 1
            elif (step["to"],step["from"]) in all_cities.keys() :
                all_cities[(step["to"],step["from"])] += 1
            else :
                all_cities[(step["from"],step["to"])] = 1
            tot += 1
    over_treshold = []
    tot = max(tot,1)
    for pair in all_cities.keys():
        if all_cities[pair]/tot > threshold :
            over_treshold.append(pair)
    return over_treshold
    

def generate_recStandardForOneDriver(nb_routes, freq_items, freq_pairs):
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
    recstd_routes = []
    for i in range(nb_routes):
        recstd_routes.append({
            "route": dataGenerator.newStdGenerator.generate_new_route(freq_pairs, cleaned_freq_items)
        })
    return recstd_routes

if __name__ == "__main__":
    # Read and parse standard routes
    with open("./data/standard.json", "r") as standard_file:
        standard_routes = json.load(standard_file)
    # Read and parse actual routes
    with open("./data/actual.json", "r") as actual_file:
        actual_routes = json.load(actual_file)
    city_freq = city_frequency(actual_routes)
    drivers = get_drivers(actual_routes)
    start = t.time()
    perfect_routes = []
    for driver in drivers :
        actualRoutesDriver = get_routes_per_driver(actual_routes,driver)
        frequent_itemsets, rules = FIandAssoRulesForOneDriver(0.2, 0.5, actualRoutesDriver, driver)
        #frequent_itemsets.to_csv("./data/csv/freq_items_driver1.csv", index=False)
        #rules.to_csv("./data/csv/asso_rules_driver1.csv", index=False)
        fav_cit_driver = fav_cities_driver(actualRoutesDriver,city_freq,1.2)
        fav_pairs_driver = pairs_from_favs(fav_cit_driver)
        recstd_route = generate_recStandardForOneDriver(1, frequent_itemsets,fav_pairs_driver)
        perfect_routes.append({"driver":driver,"route":recstd_route[0]["route"]})
        #print(driver + " done")
        #print(t.time()-start)
    # save data
    frequent_itemsets.to_json(f"./data/freq_items_driver{driver}.json", orient="records")
    with open(f"./results/perfectRoute.json", "w") as recstd_driver_file:
        json.dump(perfect_routes, recstd_driver_file)