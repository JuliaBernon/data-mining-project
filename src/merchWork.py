import json

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth
import pandas as pd

import matplotlib.pyplot as plt

with open("./data/actual.json") as actual_file:
    actual_routes = json.load(actual_file)


# function to transform a route into a list of merchandises for each step
def route_to_merchandises(route):
    '''
    Returns a list of merchandises for each step in a route.
    route : list(dict(str, str))
    '''
    merchandises = []
    for i in range(len(route)):
        merchandises.append(route[i]["merchandise"])
    return merchandises

def route_to_list_merch(route):
    '''
    Returns a list of dictionaries with the merchandise types for each step in a route.
    route : list(dict(str, str))
    '''
    route_merchandise_types = []
    for i, dictionary in enumerate(route_to_merchandises(route)):
        merchandise_types = list(dictionary.keys())

        route_merchandise_types.append(merchandise_types)
    return route_merchandise_types

# select one route from actual.json
route = actual_routes[0]["route"]
print(route_to_list_merch(route))

te = TransactionEncoder()
te_ary = te.fit(route_to_list_merch(route)).transform(route_to_list_merch(route))
df = pd.DataFrame(te_ary, columns=te.columns_)

freq_items_for1 = apriori(df, min_support=0.3, use_colnames=True)
# element must appear at least 75% of the time to be considered frequent
print(freq_items_for1)

association_rules_for1 = association_rules(freq_items_for1, metric="confidence", min_threshold=0.3)
print(association_rules_for1)

# save data into csv files to make it easier to read
# freq_items_for1.to_csv("./data/freq_items_for1.csv")
# association_rules_for1.to_csv("./data/association_rules_for1.csv")

# plot support vs confidence
plt.scatter(association_rules_for1["support"], association_rules_for1["confidence"], alpha=0.5)
plt.xlabel("support")
plt.ylabel("confidence")
plt.title("Support vs Confidence")
plt.show()