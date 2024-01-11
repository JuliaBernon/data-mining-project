import json
import math
from routes_distance import compute_distance
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
    -list of couples driver/ranking of standard routes
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
    Returns a list of the best standard routes based on the given actual routes per driver.

    Parameters:
    - actuals_driver (list): List of route ids for a driver.
    - dict_actuals (dict): Dictionary containing information about actual routes.
    - dict_standard_routes (dict): Dictionary containing information about standard routes.

    Returns:
    - list: List of the best standard routes.

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
    for i in range(len(list_dist_moy)):
        list_dist_moy[i] = list_dist_moy[i][0]
    if len(list_dist_moy) >= 5 :
        #return list_dist_moy[:5]
        return list_dist_moy
    else :
        return list_dist_moy

def dist_moy_to_a_standard_route(standard_route, actuals, dict_actuals, dict_standard_routes):
    '''
    Calculate the average distance between a standard route and a list of actual routes.

    Parameters:
    - standard_route (int): The ID of the standard route.
    - actuals (list): A list of route IDs.
    - dict_actuals (dict): A dictionary mapping route IDs to route information.
    - dict_standard_routes (dict): A dictionary mapping standard route IDs to route information.

    Returns:
    - float: The average distance between the standard route and the actual routes. If the list of actual routes is empty, returns math.inf.
    '''
    tot_dist = 0
    for actual in actuals :
        tot_dist += compute_distance(dict_standard_routes[standard_route], dict_actuals[actual]["route"])
    if len(actuals) > 0 :
        return tot_dist/len(actuals)
    else :
        return math.inf

rankings = get_rankings(dict_actuals,dict_standard_routes)

# save data into std_rankings.json
if __name__ == "__main__":
    with open("./data/std_rankings.json", "w") as rankings_file:
        json.dump(rankings, rankings_file, indent=4)

print(f"question_2 done : {len(rankings)} drivers ranked in ./data/std_rankings.json")