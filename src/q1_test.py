### This file is used to print all the data in a readable format ###
import json
import time
# import matplotlib.pyplot as plt
from routes_distance import compute_distance

start_time = time.time()

# Read and parse standard routes
with open("./data/standard.json", "r") as standard_file:
    standard_routes = json.load(standard_file)
nb_std_routes = len(standard_routes)

with open("./results/recStandard16000.json", "r") as recstd_file:
    recstd_routes = json.load(recstd_file)
nb_recstd_routes = len(recstd_routes)

# Read and parse actual routes
with open("./data/actual16000.json", "r") as actual_file:
    actual_routes = json.load(actual_file)
nb_act_routes = len(actual_routes)

with open("./data/newActual16000.json", "r") as new_actual_file:
    new_actual_routes = json.load(new_actual_file)
nb_new_act_routes = len(new_actual_routes)

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

## Compute mean, standard deviation, min, max
mean = sum(distances) / len(distances)
mean_bis = sum(distances_bis) / len(distances_bis)
std = (sum([(dist - mean)**2 for dist in distances]) / len(distances))**(1/2)
std_bis = (sum([(dist_bis - mean_bis)**2 for dist_bis in distances_bis]) / len(distances_bis))**(1/2)
min_dist = min(distances)
min_dist_bis = min(distances_bis)
max_dist = max(distances)
max_dist_bis = max(distances_bis)

print(f"Mean distance between actual routes and standard routes: {mean}")
print(f"Mean distance between new actual routes and new standard routes: {mean_bis}")
print("\n")
print(f"Standard deviation of distances between actual routes and standard routes: {std}")
print(f"Standard deviation of distances between new actual routes and new standard routes: {std_bis}")
print("\n")
print(f"Minimum distance between actual routes and standard routes: {min_dist}")
print(f"Minimum distance between new actual routes and new standard routes: {min_dist_bis}")
print("\n")
print(f"Maximum distance between actual routes and standard routes: {max_dist}")
print(f"Maximum distance between new actual routes and new standard routes: {max_dist_bis}")
print("\n")

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

# write data in txt file
# name of the file is date and time of execution
file_name = time.strftime("%Y%m%d-%H%M%S")
with open(f"./results/tests/distances/std500bis/{file_name}.txt", "w") as distances_file:
    distances_file.write("Threshold : 0.8, Support : 0.3, Max_len : 3\n")
    distances_file.write(f"{nb_std_routes} standard routes, {nb_act_routes} actual routes, {nb_new_act_routes} new actual routes, {nb_recstd_routes} rec standard routes\n\n")
    distances_file.write(f"Mean distance between actual routes and standard routes: {mean}\n")
    distances_file.write(f"Mean distance between new actual routes and new standard routes: {mean_bis}\n")
    distances_file.write("\n")
    distances_file.write(f"Standard deviation of distances between actual routes and standard routes: {std}\n")
    distances_file.write(f"Standard deviation of distances between new actual routes and new standard routes: {std_bis}\n")
    distances_file.write("\n")
    distances_file.write(f"Minimum distance between actual routes and standard routes: {min_dist}\n")
    distances_file.write(f"Minimum distance between new actual routes and new standard routes: {min_dist_bis}\n")
    distances_file.write("\n")
    distances_file.write(f"Maximum distance between actual routes and standard routes: {max_dist}\n")
    distances_file.write(f"Maximum distance between new actual routes and new standard routes: {max_dist_bis}\n")
    distances_file.write("\n")
    distances_file.write(f"Execution time: {execution_time} seconds\n")


# # subplot distances and distances_bis
# plt.subplot(1, 2, 1)
# subplt1 = plt.hist(distances, bins=100)
# plt.title("Distances between actual routes and standard routes")
# plt.xlabel("Distance")
# plt.ylabel("Frequency")
# plt.subplot(1, 2, 2)
# subplt2 = plt.hist(distances_bis, bins=100)
# plt.title("Distances between new actual routes and new standard routes")
# plt.xlabel("Distance")
# plt.ylabel("Frequency")
# plt.show()