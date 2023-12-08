### Frequent itemsets and association rules ###
### This file contains functions and scripts in order to determine the association rules between merchandise types. ###

import json
import pandas as pd
import matplotlib.pyplot as plt
import sys

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth

# Two functions to transform a route into a list of merchandises for each step
def route_to_merchandises(route):
    '''
    Returns a list of merchandises for each step in a route.
    route : list(dict(str, str))
    '''
    merchandises = []
    for i in range(len(route)):
        merchandises.append(route[i]["merchandise"])
    return merchandises

# print(route_to_merchandises(actual_routes[0]["route"]))
# [{'water': 3, 'milk': 41, 'sugar': 6, 'honey': 17, 'chocolate': 26},...]

def route_to_list_merch(route):
    '''
    Returns a list of dictionaries with the merchandise types for each step in a route.
    route : list(dict(str, str))
    '''
    route_merchandise_types = []
    for i, dictionary in enumerate(route_to_merchandises(route)):
        merchandise_types = list(dictionary.keys())

        route_merchandise_types.append(merchandise_types)
        # route_merchandise_types[i].append(route[i]["from"])
        # route_merchandise_types[i].append(route[i]["to"])
    return route_merchandise_types

def FIandAssoRules(support, threshold, maxLen, actualFile):
    '''
    Returns the frequent itemsets and association rules for a given threshold and a given actualFile.
    support : float
    threshold : float
    actualFile : str
    '''
    with open(actualFile) as actual_file:
        actual_routes = json.load(actual_file)

    # Transform all the routes of actual.json into a list of lists
    all_routes = []
    for i in range(len(actual_routes)):
        all_routes.append(route_to_list_merch(actual_routes[i]["route"]))

    for route in all_routes:
        if route ==  []:
            all_routes.remove(route)

    # Flatten the list of lists if necessary
    all_routes = [[item for sublist in route for item in sublist] if isinstance(route[0], list) else route for route in all_routes]

    te = TransactionEncoder()
    te_ary = te.fit(all_routes).transform(all_routes)
    df = pd.DataFrame(te_ary, columns=te.columns_)

    freq_items = apriori(df, min_support=support, use_colnames=True, max_len = maxLen)
    asso_rules = association_rules(freq_items, metric="confidence", min_threshold=threshold)

    return freq_items, asso_rules

if len(sys.argv) > 1:
    support = float(sys.argv[1])
    threshold = float(sys.argv[2])
    maxLen = float(sys.argv[3])
    actualFile = sys.argv[4]
    FIname_to_save = sys.argv[5]
    ARname_to_save = sys.argv[6]
    FIname_to_save_json = sys.argv[7]
    freq_items, asso_rules = FIandAssoRules(support, threshold, maxLen, actualFile)
else:
    freq_items, asso_rules = FIandAssoRules(0.75, 0.3, 3, "./data/actual.json")
    FIname_to_save = "./data/csv/freq_items.csv"
    ARname_to_save = "./data/csv/asso_rules.csv"
    FIname_to_save_json = "./data/freq_items.json"

# Save data into csv and json files
if __name__ == "__main__":
    freq_items.to_csv(FIname_to_save, index=False)
    asso_rules.to_csv(ARname_to_save, index=False)
    freq_items.to_json(FIname_to_save_json, orient="records", indent=4, lines=True)

# freq_items, asso_rules = FIandAssoRules(0.75, 0.3, 3, "./data/actual.json")

# # subplots support vs confidence, support vs lift, confidence vs lift
# fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
# fig.suptitle('Association Rules')
# ax1.scatter(asso_rules["support"], asso_rules["confidence"], alpha=0.5)
# ax1.set_xlabel("support")
# ax1.set_ylabel("confidence")
# ax2.scatter(asso_rules["support"], asso_rules["lift"], alpha=0.5)
# ax2.set_xlabel("support")
# ax2.set_ylabel("lift")
# ax3.scatter(asso_rules["confidence"], asso_rules["lift"], alpha=0.5)
# ax3.set_xlabel("confidence")
# ax3.set_ylabel("lift")
# plt.show()

