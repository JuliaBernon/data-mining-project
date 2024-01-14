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

    Parameters:
    actual_routes (list[dict[str, str]]): A list of dictionaries representing actual routes.

    Returns:
    list[str]: A list of all the drivers in actual_routes.
    '''
    drivers = []
    for route in actual_routes:
        if route["driver"] not in drivers:
            drivers.append(route["driver"])
    return drivers

def get_routes_per_driver(actual_routes, driver):
    '''
    Returns a list of all the routes done by a given driver.

    Parameters:
    actual_routes (list[dict[str, str]]): A list of dictionaries representing the actual routes.
    driver (str): The name of the driver.

    Returns:
    list[dict[str, str]]: A list of dictionaries representing the routes done by the given driver.
    '''
    routes_per_driver = []
    for route in actual_routes:
        if route["driver"] == driver:
            routes_per_driver.append(route)
    return routes_per_driver

# create a function to get the FIs and ARs for a given driver
def FIandAssoRulesForOneDriver(support, threshold, actualRoutesDriver, driver):
    """
    Calculates frequent itemsets and association rules for a given driver's routes.

    Parameters:
    support (float): Minimum support threshold for frequent itemsets.
    threshold (float): Minimum confidence threshold for association rules.
    actualRoutesDriver (list): List of dictionaries containing the actual routes for the driver.
    driver (str): Name of the driver.

    Returns:
    frequent_itemsets (DataFrame): DataFrame containing the frequent itemsets.
    rules (DataFrame): DataFrame containing the association rules.
    """
    all_routes = []
    for i in range(len(actualRoutesDriver)):
        all_routes.append(route_to_list_merch(actualRoutesDriver[i]["route"]))
    temp = []
    for route in all_routes:
        if route !=  []:
            temp.append(route)
    all_routes = temp
    all_routes = [[item for sublist in route for item in sublist] if isinstance(route[0], list) else route for route in all_routes]
    te = TransactionEncoder()
    te_ary = te.fit(all_routes).transform(all_routes)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    frequent_itemsets = apriori(df, min_support=support, use_colnames=True, max_len=3)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=threshold)
    return frequent_itemsets, rules

def city_frequency(routes):
    """
    Calculates the frequency of each city in the given routes.

    Args:
        routes (list): A list of routes, where each route is a dictionary.

    Returns:
        dict: A dictionary containing the frequency of each city in the routes.
    """
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
    """
    Returns a list of favorite cities for a driver based on their actual routes,
    city frequencies, and a multiplier.

    Parameters:
    actualRoutesDriver (list): List of actual routes taken by the driver.
    city_freq (dict): Dictionary containing the frequency of each city in the actual routes.
    mult (float): Multiplier used to determine the threshold for a favorite city.

    Returns:
    list: List of favorite cities for the driver.
    """
    freqs_driver = city_frequency(actualRoutesDriver)
    fav_cities = []
    backup_cities = []
    for city in freqs_driver.keys() :
        if freqs_driver[city] >= mult*city_freq[city]:
            fav_cities.append(city)
        elif freqs_driver[city] >= city_freq[city] :
            backup_cities.append([city,freqs_driver[city]/city_freq[city]])
    backup_cities.sort(key=lambda tup : tup[1],reverse=True)
    stop = False
    while len(fav_cities)<2 and len(backup_cities) >= len(fav_cities)+1:
        fav_cities.append(backup_cities[len(fav_cities)][0])
    return fav_cities

def pairs_from_favs(fav_cities):
    """
    Generate pairs of favorite cities from a given list of favorite cities.

    Args:
        fav_cities (list): A list of favorite cities.

    Returns:
        list: A list of pairs, where each pair consists of two favorite cities.

    Example:
        >>> fav_cities = ['New York', 'Paris', 'Tokyo']
        >>> pairs_from_favs(fav_cities)
        [('New York', 'Paris'), ('New York', 'Tokyo'), ('Paris', 'New York'), ('Paris', 'Tokyo'), ('Tokyo', 'New York'), ('Tokyo', 'Paris')]
    """
    if len(fav_cities)==1:
        return([(fav_cities[0],fav_cities[0])])
    pairs = []
    for i in range(len(fav_cities)):
        for j in range(len(fav_cities)):
            if i != j :
                pairs.append((fav_cities[i],fav_cities[j]))
    return pairs

def generate_recStandardForOneDriver(nb_routes, freq_items, freq_pairs):
    '''
    Generate a new standard route, given a set of pairs of cities and merchandise types

    Parameters:
    nb_routes (int): The number of routes to generate
    freq_items (DataFrame): DataFrame containing the frequent merchandise types and itemsets
    freq_pairs (DataFrame): DataFrame containing the frequent pairs of cities

    Returns:
    List[Dict[str, Any]]: A list of dictionaries representing the generated routes
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

def run_q3():
    # Read and parse standard routes
    with open("./data/standard.json", "r") as standard_file:
        standard_routes = json.load(standard_file)
    # Read and parse actual routes
    with open("./data/actual.json", "r") as actual_file:
        actual_routes = json.load(actual_file)
    city_freq = city_frequency(standard_routes)
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
        json.dump(perfect_routes, recstd_driver_file, indent=4)
    print(f"Perfect routes generated in ./results/perfectRoute.json")

if __name__ == "__main__":
    run_q3()
#unused
def freq_cities_driver(actualRoutesDriver,number = 4,threshold = None):
    """
    Calculates the most frequent cities visited by a driver based on their routes.

    Parameters:
    actualRoutesDriver (list): A list of dictionaries representing the routes taken by the driver.
    number (int, optional): The number of most frequent cities to return. Defaults to 4.
    threshold (int, optional): The minimum frequency threshold for a city to be considered. Defaults to None.

    Returns:
    list: A list of the most frequent cities visited by the driver.
    """
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
    """
    Calculates the most frequent pairs of cities visited by a driver based on their routes.

    Parameters:
    actualRoutesDriver (list): A list of dictionaries representing the routes taken by the driver.
    threshold (float): The minimum frequency threshold for a pair of cities to be considered.

    Returns:
    list: A list of the most frequent pairs of cities visited by the driver.
    """
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
    