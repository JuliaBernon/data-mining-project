import json
import math

#get the standard routes
with open("./data/standard.json", "r") as standard_file:
    standards = json.load(standard_file)
dict_standard_routes = {} 
for standard in standards :
    dict_standard_routes[standard["id"]] = standard["route"]

#get the new standard routes
with open("./data/standard.json", "r") as new_standard_file:
    new_standards = json.load(new_standard_file)

#get the rankings routes
with open("./data/std_rankings.json", "r") as rankings_file:
    rankings = json.load(rankings_file)

from random import*
def dist_between_two_routes(route1,route2):
    return randint(1,10)

def question2(rankings,new_standards,dict_standard_routes):
    dict_drivers = {}
    for driver in rankings.keys():
        list_driver = []
        for route in new_standards :
            list_dist = []
            for std in rankings[driver]:
                list_dist.append([std,dist_between_two_routes(dict_standard_routes[std],route["route"])])
            list_dist.sort(key=lambda tup: tup[1])
            list_driver.append([route["id"],list_dist[0][0]])
        list_driver.sort(key=lambda tup: rankings[driver].index(tup[1]))
        if len(list_driver) >= 5 :
            list_driver = list_driver[:5]
            #return list_dist_moy
        for i in range(len(list_driver)) :
            list_driver[i] = list_driver[i][0]
        dict_drivers[driver]=list_driver
    return dict_drivers

q2 = question2(rankings,new_standards,dict_standard_routes)

# save data into q2.json
if __name__ == "__main__":
    with open("./data/q2.json", "w") as q2_file:
        json.dump(q2, q2_file, indent=4)