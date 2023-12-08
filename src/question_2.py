import json
from routes_distance import compute_distance
import time as t

#get the standard routes
with open("./data/standard.json", "r") as standard_file:
    standards = json.load(standard_file)
dict_standard_routes = {} 
for standard in standards :
    dict_standard_routes[standard["id"]] = standard["route"]

#get the new standard routes
with open("./results/recStandard.json", "r") as new_standard_file:
    new_standards = json.load(new_standard_file)

#get the rankings
with open("./data/std_rankings.json", "r") as rankings_file:
    rankings = json.load(rankings_file)

def question2(rankings,new_standards,dict_standard_routes):
    start = t.time()
    dict_drivers = {}
    dicts_dists = {}
    """ for route in new_standards :
        dict_dists_routes = {}
        for std in dict_standard_routes.keys() :
            dict_dists_routes[std] = compute_distance(dict_standard_routes[std],route["route"])
        dicts_dists[route["id"]] = dict_dists_routes
        print(route["id"])
        print(t.time()-start) """
    for driver in rankings.keys():
        list_driver = []
        for route in new_standards :
            list_dist = []
            for std in rankings[driver]:
                list_dist.append([std,compute_distance(dict_standard_routes[std],route["route"])])
                #list_dist.append([std,dicts_dists[route["id"]][std]])
            #print(route["id"])
            #print(list_dist)
            list_dist.sort(key=lambda tup: tup[1])
            #print(list_dist)
            list_driver.append([route["id"],list_dist[0][0],list_dist[0][1]])
            #print(route["id"])
            #print(t.time()-start)
        list_driver.sort(key=lambda tup: tup[2])
        list_driver.sort(key=lambda tup: rankings[driver].index(tup[1]))
        if len(list_driver) >= 5 :
            list_driver = list_driver[:5]
            #return list_dist_moy
        for i in range(len(list_driver)) :
            list_driver[i] = list_driver[i][0]
        dict_drivers[driver]=list_driver
        print(driver)
        print(t.time()-start)
    return dict_drivers

q2 = question2(rankings,new_standards,dict_standard_routes)

# save data into q2.json
if __name__ == "__main__":
    with open("./data/q2.json", "w") as q2_file:
        json.dump(q2, q2_file, indent=4)

print("q2 done")