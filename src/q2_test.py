import json
import math
from dataGenerator.actualGenerator import generate_actual_route
from routes_distance import compute_distance

#get the drivers
with open("./data/drivers.json", "r") as drivers_file:
    drivers = json.load(drivers_file)

#get the new standard routes
with open("./data/recStandard.json", "r") as new_standard_file:
    new_standards = json.load(new_standard_file)

#get the q2 results
with open("./data/q2.json", "r") as q2_file:
    q2_res = json.load(q2_file)

# read and parse cities.json
with open("./data/cities.json", "r") as cities_file:
    cities = json.load(cities_file)

# read and parse merchTypes.json
with open("./data/merchTypes.json", "r") as merchTypes_file:
    merchandise_types = json.load(merchTypes_file)

def test_q2(drivers,new_standards,q2_res):
    dict_test = {}
    for driver in drivers :
        true_ranking = []
        for standard_route in new_standards :
            avg = 0
            for i in range(10):
                avg += compute_distance(generate_actual_route(standard_route["route"], cities, merchandise_types, driver),standard_route["route"])
            avg = avg/10
            true_ranking.append([standard_route["id"],avg])
        true_ranking.sort(key=lambda tup: tup[1])
        for i in range(len(true_ranking)):
            true_ranking[i] = true_ranking[i][0]
        true_res = []
        res_q2 = q2_res[driver["id"]]
        for std in res_q2 :
            true_res.append(true_ranking.index(std))
        dict_test[driver["id"]] = true_res
    return dict_test

print(test_q2(drivers,new_standards,q2_res))
    