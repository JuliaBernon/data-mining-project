### Merchandise types analysis ###
### This file contains functions and scripts in order to determine the association rules between merchandise types. ###

import json
import pandas as pd
import matplotlib.pyplot as plt

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth

with open("./data/actual.json") as actual_file:
    actual_routes = json.load(actual_file)

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

# print(route_to_list_merch(actual_routes[0]["route"]))
# [['water', 'milk', 'sugar', 'honey', 'chocolate', 'Perugia', 'Milan'],...]

all_merch = []
for actual_route in actual_routes:
    all_merch.append(route_to_list_merch(actual_route["route"]))
# print(all_merch)

# Transform all the routes of actual.json into a list of lists
all_routes = []
for i in range(len(actual_routes)):
    all_routes.append(route_to_list_merch(actual_routes[i]["route"]))

for route in all_routes:
    if route ==  []:
        all_routes.remove(route)

# print(all_routes)

# Flatten the list of lists if necessary
all_routes = [[item for sublist in route for item in sublist] if isinstance(route[0], list) else route for route in all_routes]

te = TransactionEncoder()
te_ary = te.fit(all_routes).transform(all_routes)
df = pd.DataFrame(te_ary, columns=te.columns_)
# print(df)

freq_items = apriori(df, min_support=0.6, use_colnames=True, max_len = 3) # don't go below 0.6 !
asso_rules = association_rules(freq_items, metric="confidence", min_threshold=0.3)

print(freq_items)
# print("\n")
print(asso_rules)

# save into csv files
freq_items.to_csv("./data/freq_items.csv")
asso_rules.to_csv("./data/asso_rules.csv")

# Keeping only the rules with a confidence above 0.925 and a lift above 1.17
selected_rules = asso_rules[(asso_rules['confidence'] > 0.6) & (asso_rules['lift'] > 1.01)]
# print(selected_rules)

# sublots support vs confidence, support vs lift, and lift vs confidence
fig, ax = plt.subplots(2, 3, figsize=(15, 10))
ax[0, 0].scatter(asso_rules['support'], asso_rules['confidence'], alpha=0.5)
ax[0, 0].set_xlabel('support')
ax[0, 0].set_ylabel('confidence')
ax[0, 0].set_title('Support vs Confidence')
ax[0, 1].scatter(asso_rules['support'], asso_rules['lift'], alpha=0.5)
ax[0, 1].set_xlabel('support')
ax[0, 1].set_ylabel('lift')
ax[0, 1].set_title('Support vs Lift')
ax[0, 2].scatter(asso_rules['lift'], asso_rules['confidence'], alpha=0.5)
ax[0, 2].set_xlabel('lift')
ax[0, 2].set_ylabel('confidence')
ax[0, 2].set_title('Lift vs Confidence')

# subplots with confidence > 0.925 and lift > 1.17
ax[1, 0].scatter(selected_rules['support'], selected_rules['confidence'], alpha=0.5)
ax[1, 0].set_xlabel('support')
ax[1, 0].set_ylabel('confidence')
ax[1, 0].set_title('Support vs Confidence')
ax[1, 1].scatter(selected_rules['support'], selected_rules['lift'], alpha=0.5)
ax[1, 1].set_xlabel('support')
ax[1, 1].set_ylabel('lift')
ax[1, 1].set_title('Support vs Lift')
ax[1, 2].scatter(selected_rules['lift'], selected_rules['confidence'], alpha=0.5)
ax[1, 2].set_xlabel('lift')
ax[1, 2].set_ylabel('confidence')
ax[1, 2].set_title('Lift vs Confidence')

plt.tight_layout()
plt.show()


