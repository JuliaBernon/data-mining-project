## This file contains functions to analyze the different routes a driver has taken ##

import json
import pandas as pd
import matplotlib.pyplot as plt

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
# from mlxtend.frequent_patterns import fpgrowth
from merchFIAndAssoRules import route_to_list_merch

# Read and parse standard routes
with open("./data/standard.json", "r") as standard_file:
    standard_routes = json.load(standard_file)

# Read and parse actual routes
with open("./data/actual.json", "r") as actual_file:
    actual_routes = json.load(actual_file)


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

# for driver in get_drivers(actual_routes):
#     print(f"Driver {driver} :")
#     print(get_routes_per_driver(actual_routes, driver))

# create a function to get the FIs and ARs for a given driver
def FIandAssoRulesForOneDriver(support, threshold, maxLen, actualRoutesDriver, driver):
    
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

    frequent_itemsets = apriori(df, min_support=support, use_colnames=True, max_len=maxLen)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=threshold)

    return frequent_itemsets, rules

drivers = get_drivers(actual_routes)
# print(drivers)
actual_routes_driver = get_routes_per_driver(actual_routes, drivers[0])
with open("./data/actual_driver1.json", "w") as actual_driver_file:
    json.dump(actual_routes_driver, actual_driver_file)
# print(actual_routes_driver)
frequent_itemsets, rules = FIandAssoRulesForOneDriver(0.8, 0.5, 3, actual_routes_driver, drivers[0])
print(frequent_itemsets, rules)

# save data
frequent_itemsets.to_csv("./data/csv/freq_items_driver1.csv", index=False)
rules.to_csv("./data/csv/asso_rules_driver1.csv", index=False)
frequent_itemsets.to_json("./data/freq_items_driver1.json", orient="records")

# # subplots support vs confidence, support vs lift, confidence vs lift
# plt.subplot(1, 3, 1)
# plt.scatter(rules["support"], rules["confidence"], alpha=0.5)
# plt.xlabel("support")
# plt.ylabel("confidence")
# plt.subplot(1, 3, 2)
# plt.scatter(rules["support"], rules["lift"], alpha=0.5)
# plt.xlabel("support")
# plt.ylabel("lift")
# plt.subplot(1, 3, 3)
# plt.scatter(rules["confidence"], rules["lift"], alpha=0.5)
# plt.xlabel("confidence")
# plt.ylabel("lift")
# plt.show()
