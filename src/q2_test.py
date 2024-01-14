### Test the q2 function by calculating the average error for each driver.

import json
import time as t
from dataGenerator.actualGenerator import generate_actual_route
from routes_distance import compute_distance
from q2_driver import run_q2
from exe_script import exe_script

def test_q2(drivers,new_standards,q2_res,cities,merchandise_types):
    """
    Test the q2 function by calculating the average error for each driver.

    Parameters:
    drivers (list): A list of driver objects.
    new_standards (list): A list of new standards.
    q2_res (dict): A dictionary containing the q2 results.

    Returns:
    dict: A dictionary containing the average error for each driver and the tps_ex value.
    """
    tps_ex = q2_res.pop("tps_ex")
    debut = t.time()
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
        if driver["id"] in q2_res.keys():
            res_q2 = q2_res[driver["id"]]
            for std in res_q2 :
                true_res.append(true_ranking.index(std))
            dict_test[driver["id"]] = true_res
            #print(driver["id"])
            #print(t.time()-debut)
    avg = 0
    nb_driver = 0
    for driver in dict_test.keys():
        avg_driver = 0
        for i in range(5):
            avg_driver += dict_test[driver][i]-(i+1)
        avg_driver = avg_driver/5
        avg += avg_driver
        nb_driver += 1
    avg = avg/nb_driver
    dict_test["average error"] = avg
    return dict_test,tps_ex

def one_test():
    #exec q2
    start = t.time()
    run_q2()
    tps_ex = t.time()-start
    #get the drivers
    with open("./data/drivers.json", "r") as drivers_file:
        drivers = json.load(drivers_file)
    #get the new standard routes
    with open("./results/recStandard.json", "r") as new_standard_file:
        new_standards = json.load(new_standard_file)
    #get the new standard routes
    with open("./data/actual.json", "r") as actual_file:
        actuals = json.load(actual_file)
    #get the q2 results
    with open("./results/driver.json", "r") as q2_file:
        q2_res = json.load(q2_file)
    # read and parse cities.json
    with open("./data/cities.json", "r") as cities_file:
        cities = json.load(cities_file)
    # read and parse merchTypes.json
    with open("./data/merchTypes.json", "r") as merchTypes_file:
        merchandise_types = json.load(merchTypes_file)
    #run the test
    q2_test,tps_test = test_q2(drivers,new_standards,q2_res,cities,merchandise_types)
    # save data into q2.json
    with open("./data/q2_test.json", "w") as q2_test_file:
        json.dump(q2_test, q2_test_file, indent=4)
    # write data in txt file
    # name of the file is date and time of execution
    file_name = t.strftime("%Y%m%d-%H%M%S")
    with open(f"./results/tests/q2/{file_name}.txt", "w") as fi:
        fi.write("Threshold : 0.8, Support : 0.3, Max_len : 3\n")
        fi.write(f"nb_drivers :\n{str(len(drivers))}\n")
        fi.write(f"nb_max_merch :\n{str(10)}\n")
        fi.write(f"nb_standards :\n{str(len(new_standards))}\n")
        fi.write(f"nb_actuals :\n{str(len(actuals))}\n")
        fi.write(f"nb_cities :\n{str(len(cities))}\n")
        fi.write(f"nb_merchtypes :\n{str(len(merchandise_types))}\n")
        fi.write(f"average error :\n{str(q2_test['average error'])}\n")
        fi.write(f"execution time :\n{str(tps_ex)}\n")
        fi.write(f"test time :\n{str(tps_test)}\n")
    print(f"q2_test done : {len(q2_test)} drivers tested in ./data/q2_test.json")

def multiple_tests(dict_standard_actual):
    for key in dict_standard_actual.keys():
        for i in dict_standard_actual[key]:
            print(f"Test q2 pour {key} standards et {i} actuals :")
            exe_script(key,i)
            one_test()

if __name__ == "__main__":
    #one_test()
    dict_standard_actual = {100:[100,200,300,400,500,1000,2000,4000,8000,10000,15000,20000],500:[500,1000,2000,4000,8000,16000,32000]}
    multiple_tests(dict_standard_actual)

   