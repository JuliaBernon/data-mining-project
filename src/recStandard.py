import json
import pandas as pd
import dataGenerator.newStdGenerator
import matplotlib.pyplot as plt

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth

### Read and parse data ###

with open("./data/actual.json") as actual_file:
    actual_routes = json.load(actual_file)

with open("./data/merchTypes.json","r") as merchTypes_file:
    merchandise_types = json.load(merchTypes_file)


### Generating a new route ###

# # generate recStandard.json
# nb_recstd_routes = 100 # define the number of standard routes
# recstd_routes = []
# for i in range(nb_recstd_routes):
#     recstd_routes.append({
#         "id": f"r{i + 1}",
#         "route": dataGenerator.newStdGenerator.generate_new_route(most_frequent_pairs, merchandise_types)
#     })

# # save data into recStandard.json
# with open("./data/recStandard.json", "w") as recstd_file:
#     json.dump(recstd_routes, recstd_file, indent=4)
