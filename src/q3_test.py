### Test the q2 function by making the driver do the road several times and compare with it's average deviation.

import json
import time as t
from dataGenerator.actualGenerator import generate_actual_route
from routes_distance import compute_distance
from q3_perfectRoute import run_q3
from exe_script import exe_script_wo_ar

def q3_test(q3_res,dict_drivers,actual_routes,dict_standard_routes,cities,merchandise_types):
    q3_test = {}
    tot_avg = 0
    for route in q3_res:
        driver_id = route["driver"]
        driver = dict_drivers[driver_id]
        perfect_avg = 0
        for i in range(10):
            perfect_avg+=compute_distance(generate_actual_route(route["route"],cities,merchandise_types,driver),route["route"])
        perfect_avg = perfect_avg/10
        nb_act = 0
        all_avg = 0
        for route in actual_routes:
            if route["driver"] == driver_id :
                nb_act += 1
                all_avg += compute_distance(route["route"],dict_standard_routes[route["sroute"]])
        all_avg = all_avg/max(nb_act,1)
        if all_avg == 0 :
            q3_test[driver_id] = None
        else :
            q3_test[driver_id] = 1-(perfect_avg/all_avg)
            tot_avg += 1-(perfect_avg/all_avg)
    q3_test["all"] = tot_avg/len(q3_test.keys())
    with open(f"./data/q3_test.json", "w") as q3_test_file:
            json.dump(q3_test, q3_test_file, indent=4)
    return q3_test

def one_test(cities,merchandise_types):
    #exec q3
    start = t.time()
    run_q3()
    tps_ex = t.time()-start
    # read and parse drivers.json
    with open("./data/drivers.json", "r") as drivers_file:
        drivers = json.load(drivers_file)
        dict_drivers = {} 
        for driver in drivers :
            dict_drivers[driver["id"]] = driver
    # Read and parse actual routes
    with open("./data/actual.json", "r") as actual_file:
        actual_routes = json.load(actual_file)
    #get the standard routes
        with open("./data/standard.json", "r") as standard_file:
            standards = json.load(standard_file)
        dict_standard_routes = {} 
        for standard in standards :
            dict_standard_routes[standard["id"]] = standard["route"]
    # get q3 results
    with open("./results/perfectRoute.json", "r") as q3_file:
        q3_res = json.load(q3_file)
    start = t.time()
    q3_res = q3_test(q3_res,dict_drivers,actual_routes,dict_standard_routes,cities,merchandise_types)
    tps_test = t.time()-start
    file_name = t.strftime("%Y%m%d-%H%M%S")
    with open(f"./results/tests/q3/{file_name}.txt", "w") as fi:
        fi.write("Threshold : 0.8, Support : 0.3, Max_len : 3\n")
        fi.write(f"nb_drivers :\n{str(len(drivers))}\n")
        fi.write(f"nb_max_merch :\n{str(10)}\n")
        fi.write(f"nb_standards :\n{str(len(standards))}\n")
        fi.write(f"nb_actuals :\n{str(len(actual_routes))}\n")
        fi.write(f"nb_cities :\n{str(len(cities))}\n")
        fi.write(f"nb_merchtypes :\n{str(len(merchandise_types))}\n")
        fi.write(f"average amelioration :\n{str(q3_res['all'])}\n")
        fi.write(f"execution time :\n{str(tps_ex)}\n")
        fi.write(f"test time :\n{str(tps_test)}\n")
    print(f"q3_test done : {len(q3_res)} drivers tested in ./data/q3_test.json")

def multiple_tests(dict_standard_actual):
    # read and parse cities.json
    with open("./data/cities.json", "r") as cities_file:
        cities = json.load(cities_file)
    # read and parse merchTypes.json
    with open("./data/merchTypes.json", "r") as merchTypes_file:
        merchandise_types = json.load(merchTypes_file)
    for key in dict_standard_actual.keys():
        for i in dict_standard_actual[key]:
            print(f"Test q3 pour {key} standards et {i} actuals :")
            exe_script_wo_ar(key,i)
            one_test(cities,merchandise_types)

if __name__ == "__main__":
    #one_test()
    dict_standard_actual = {100:[100,200,300,400,500,1000,2000,4000,8000,10000,15000,20000],
                            500:[500,1000,2000,4000,8000,16000,32000],
                            1000:[1000,2000,4000,8000,16000,32000]}
    multiple_tests(dict_standard_actual)
