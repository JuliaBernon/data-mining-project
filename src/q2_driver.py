import json
from routes_distance import compute_distance
import time as t
from rankings import get_rankings

def question2(rankings, new_standards, dict_standard_routes):
    """
    Compute the rankings of drivers based on their distances to new standard routes.

    Args:
        rankings (dict): A dictionary containing the rankings of drivers.
        new_standards (list): A list of new standard routes.
        dict_standard_routes (dict): A dictionary containing the standard routes.

    Returns:
        dict: A dictionary containing the rankings of drivers based on their distances to new standard routes.
    """
    start = t.time()
    dict_drivers = {}
    dicts_dists = {}
    tot = 0
    for driver in rankings.keys():
        list_driver = []
        for route in new_standards :
            list_dist = []
            for std in rankings[driver]:
                list_dist.append([std,compute_distance(dict_standard_routes[std],route["route"])])
                #list_dist.append([std,dicts_dists[route["id"]][std]])
            list_dist.sort(key=lambda tup: tup[1])
            list_driver.append([route["id"],list_dist[0][0],list_dist[0][1]])
        list_driver.sort(key=lambda tup: tup[2])
        list_driver.sort(key=lambda tup: rankings[driver].index(tup[1]))
        if len(list_driver) >= 5 :
            list_driver = list_driver[:5]
            #return list_dist_moy
        #print(list_driver)
        for i in range(len(list_driver)) :
            list_driver[i] = list_driver[i][0]
        dict_drivers[driver]=list_driver
        #print(driver)
        #print(tot)
        tot+=1
        #print(t.time()-start)
    dict_drivers["tps_ex"] = t.time()-start
    return dict_drivers

def run_q2():
    #get the standard routes
    with open("./data/standard.json", "r") as standard_file:
        standards = json.load(standard_file)
    dict_standard_routes = {} 
    for standard in standards :
        dict_standard_routes[standard["id"]] = standard["route"]

    #get the actual routes
    with open("./data/actual.json", "r") as actual_file:
        actuals = json.load(actual_file)
    dict_actuals = {}
    for actual in actuals :
        dict_actuals[actual["id"]] = actual

    #get the new standard routes
    with open("./results/recStandard.json", "r") as new_standard_file:
        new_standards = json.load(new_standard_file)
    dict_new_standard_routes = {} 
    for new_standard in new_standards :
        dict_new_standard_routes[new_standard["id"]] = new_standard["route"]

    #calculate the rankings
    rankings = get_rankings(dict_actuals,dict_standard_routes)

    #find the best routes for each driver
    q2 = question2(rankings,new_standards,dict_standard_routes)

    # save data into q2.json
    with open("./results/driver.json", "w") as q2_file:
            json.dump(q2, q2_file, indent=4)

    print(f"question2 done : {len(q2)-1} drivers ranked in ./results/driver.json")

if __name__ == "__main__":
    run_q2()