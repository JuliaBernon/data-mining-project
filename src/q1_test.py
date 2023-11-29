### This file is used to print all the data in a readable format ###

import json
import matplotlib.pyplot as plt
from routes_distance import compute_distance

# Read and parse standard routes
with open("./data/standard.json", "r") as standard_file:
    standard_routes = json.load(standard_file)

with open("./results/recStandard.json", "r") as recstd_file:
    recstd_routes = json.load(recstd_file)

# Read and parse actual routes
with open("./data/actual.json", "r") as actual_file:
    actual_routes = json.load(actual_file)

with open("./data/newActual.json", "r") as new_actual_file:
    new_actual_routes = json.load(new_actual_file)

# Read and parse drivers
with open("./data/drivers.json", "r") as drivers_file:
    drivers = json.load(drivers_file)

## Print, for each standard route, the associated actual routes
distances = []
distances_bis = []

for std_route in standard_routes:
    for act_route in actual_routes:
        if act_route["sroute"] == std_route["id"]:
            dist = compute_distance(act_route, std_route)
            distances.append(dist)
for rec_std_route in recstd_routes:
    for new_act_route in new_actual_routes:
        if new_act_route["sroute"] == rec_std_route["id"]:
            dist_bis = compute_distance(new_act_route, rec_std_route)
            distances_bis.append(dist_bis)


# print("Standard routes and associated actual routes :")
# for route in standard_routes:
#     print(f"Standard route {route['id']} :")
#     for actual_route in actual_routes:
#         if actual_route["sroute"] == route["id"]:
#             dist = compute_distance(actual_route, route)
#             distances.append(dist)
#             print(f"\tActual route {actual_route['id']} (driver {actual_route['driver']}) : {dist}")
#     print("\n")

# subplot distances and distances_bis
plt.subplot(1, 2, 1)
subplt1 = plt.hist(distances, bins=100)
plt.title("Distances between actual routes and standard routes")
plt.xlabel("Distance")
plt.ylabel("Frequency")
plt.subplot(1, 2, 2)
subplt2 = plt.hist(distances_bis, bins=100)
plt.title("Distances between new actual routes and new standard routes")
plt.xlabel("Distance")
plt.ylabel("Frequency")
plt.show()
