import json
import math
'''
Deux scénars :
-les drivers ont déja fait toutes les routes standards un nombre de fois élevé -> pour chaque route satandard on regarde la distance moyenne avec les routes actuelles basées dessus
-les drivers ont jamais vu les routes standards et elles sont assez différentes des routes standards utilisées pour fabriquer les actuelles
Parce que :
Si ont prend la route standard la plus proche en moyenne des routes actuelles ça va juste être celle qu'il a le plus fait.
-> en parler avec julia
'''

#get the actual routes
with open("./data/actual.json", "r") as actual_file:
    actuals = json.load(actual_file)
dict_actuals = {}
for actual in actuals :
    dict_actuals[actual["id"]] = actual

#get the standard routes
with open("./data/standard.json", "r") as standard_file:
    standards = json.load(standard_file)
dict_standard_routes = {} 
for standard in standards :
    dict_standard_routes[standard["id"]] = standard["route"]

#get the new standard routes
with open("./data/standard.json", "r") as new_standard_file:
    new_standards = json.load(new_standard_file)

def get_rankings(dict_actuals,dict_standard_routes):
    '''
    Input :
    -list of actual routes
    -list of standard routes
    Output :
    -list of couples driver/5 favorite standard routes
    '''
    #getting a dict of actual routes ids per driver
    actuals_per_driver = {}
    for actual in dict_actuals.values():
        if actual["driver"] not in actuals_per_driver.keys() :
            actuals_per_driver[actual["driver"]] = [actual["id"]]
        else :
            actuals_per_driver[actual["driver"]].append(actual["id"])
    
    best_routes_per_driver = {}
    for driver in actuals_per_driver.keys():
        best_routes_per_driver[driver] = best_per_driver(actuals_per_driver[driver],dict_actuals,dict_standard_routes)
    return best_routes_per_driver

def best_per_driver(actuals_driver, dict_actuals, dict_standard_routes):
    '''
    - actuals_driver : list of route ids
    '''
    #getting a dict of actual routes ids per standard route
    actuals_per_standard = {}
    for actual in actuals_driver: #actual is a route id
        if dict_actuals[actual]["sroute"] not in actuals_per_standard.keys() :
            actuals_per_standard[dict_actuals[actual]["sroute"]] = [actual]
        else :
            actuals_per_standard[dict_actuals[actual]["sroute"]].append(actual)
    list_dist_moy = []
    for sroute in actuals_per_standard.keys() :
        dist_moy = dist_moy_to_a_standard_route(sroute,actuals_per_standard[sroute],dict_actuals,dict_standard_routes)
        list_dist_moy.append([sroute,dist_moy])
    list_dist_moy.sort(key=lambda tup: tup[1])
    if len(list_dist_moy) >= 5 :
        #return list_dist_moy[:5]
        return list_dist_moy
    else :
        return list_dist_moy

def dist_moy_to_a_standard_route(standard_route,actuals,dict_actuals,dict_standard_routes,):
    '''
    - standard_route : route id
    - actuals : list of route ids
    '''
    tot_dist = 0
    for actual in actuals :
        tot_dist += dist_between_two_routes(dict_standard_routes[standard_route], dict_actuals[actual]["route"])
    if len(actuals) > 0 :
        return tot_dist/len(actuals)
    else :
        return math.inf

from random import*
def dist_between_two_routes(route1,route2):
    return randint(1,10)

def question2(rankings,new_standards,dict_standard_routes):
    dict_drivers = {}
    for driver in rankings.keys():
        list_driver = []
        for route in new_standards :
            list_dist = []
            for duo in rankings[driver]:
                list_dist.append([duo[0],dist_between_two_routes(dict_standard_routes[duo[0]],route["route"]),duo[1]])
            list_dist.sort(key=lambda tup: tup[1])
            list_driver.append([route["id"],list_dist[0]])
        list_driver.sort(key=lambda tup: tup[1][2])
        if len(list_driver) >= 5 :
            list_driver = list_driver[:5]
            #return list_dist_moy
        dict_drivers[driver]=list_driver
    return dict_drivers

rankings = get_rankings(dict_actuals,dict_standard_routes)
print(question2(rankings,new_standards,dict_standard_routes))

