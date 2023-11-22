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

freq_items = apriori(df, min_support=0.001, use_colnames=True, max_len = 3) # don't go below 0.6 !
asso_rules = association_rules(freq_items, metric="confidence", min_threshold=0.3)

print(freq_items)
# print("\n")
# # print(asso_rules)

# save into csv files
freq_items.to_csv("./data/freq_items.csv")
asso_rules.to_csv("./data/asso_rules.csv")

# Keeping only the rules with a confidence above 0.925 and a lift above 1.17
selected_rules = asso_rules[(asso_rules['confidence'] > 0.9) & (asso_rules['lift'] > 1.15)]
# print(selected_rules)
# selected_rules.to_csv("./data/selected_rules.csv")

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




### Generating combination of merchandise types for each association rule and pair of cities ###
# from itertools import combinations

# def combination_generation(association_rules, city_pairs, merchandise_types):
#     """
#     Generate combinations of merchandise types for each association rule and pair of cities.

#     Parameters:
#     - association_rules: List of association rules (DataFrame)
#     - city_pairs: List of pairs of cities
#     - merchandise_types: List of merchandise types

#     Returns:
#     - List of dictionaries, each containing a pair of cities, associated merchandise types, and rule details.
#     """
#     combinations_list = []

#     for rule_index, rule in association_rules.iterrows():
#         for city_pair in city_pairs:
#             # Generate combinations of merchandise types for each rule and city pair
#             merchandise_combinations = list(combinations(merchandise_types, rule['antecedent_len']))

#             # Create a dictionary to store the information
#             combination_info = {
#                 'city_pair': city_pair,
#                 'rule': {
#                     'antecedent': rule['antecedents'],
#                     'consequent': rule['consequents'],
#                     'confidence': rule['confidence']
#                 },
#                 'merchandise_combinations': merchandise_combinations
#             }

#             combinations_list.append(combination_info)

#     return combinations_list

# def create_route(merchandise_combination, city_pair):
#     """
#     Create a route based on a combination of merchandise types and a pair of cities.

#     Parameters:
#     - merchandise_combination: List of merchandise types
#     - city_pair: Tuple representing a pair of cities

#     Returns:
#     - Dictionary representing the created route
#     """
#     route = []

#     # Create a route entry for each merchandise type in the combination
#     for merchandise_type in merchandise_combination:
#         route_entry = {
#             'from': city_pair[0],
#             'to': city_pair[1],
#             'merchandise': {merchandise_type: 1}  # You may modify the quantity as needed
#         }
#         route.append(route_entry)

#     return route

# def create_new_routes(selected_rules, common_pairs, merchandise_types):
#     new_routes = []

#     for rule in selected_rules.itertuples(index=False):
#         for pair in common_pairs:
#             merchandise_combinations = combination_generation(rule, pair, merchandise_types)

#             for combination in merchandise_combinations:
#                 new_route = create_route(pair, combination)
#                 new_routes.append(new_route)

#     return new_routes


# ### Selecting interesting rules ###
# selected_rules = asso_rules[asso_rules["confidence"] > 0.95]
# selected_rules_list = selected_rules.values.tolist()
# print("Selected rules : ", selected_rules_list)
