### This file contains a function to generate an actual route, given a standard route ###

import random as r
import copy as cp

merch_add_or_del_min = 0
merch_add_or_del_max = 5
merch_add_max = 20

merch_modif_min = 0
merch_modif_max = 5
merch_modif_qty_max = 10

city_add_or_del_min = 0
city_add_or_del_max = 2

# function to generate a route
def generate_actual_route(standard_route, cities, merchandise_types, driver):

    '''
    Generate an actual route, given a standard route
    standard_route : List[Dict[str, Any]]

    generate_route(cities, merchandise_types) -> List[Dict[str, Any]]
    '''
    actual_route = cp.deepcopy(standard_route)
    l = len(actual_route)
    #adding or suppressing merchandise
    merch_add_or_del_number = r.randint(merch_add_or_del_min,merch_add_or_del_max)
    for i in range(merch_add_or_del_number) :
        step = r.randint(0,l-1)
        merch = r.choice(merchandise_types)
        number = r.random()
        if merch in actual_route[step]["merchandise"].keys():
            if number > driver["agenda"]["pref_merch"][merch] :
                actual_route[step]["merchandise"][merch] = 0
        else :
            if number < driver["agenda"]["pref_merch"][merch] :
                actual_route[step]["merchandise"][merch] = r.randint(1,merch_add_max)
    #transporting a little more or a little less merchandise
    merch_more_or_less_number = r.randint(merch_modif_min,merch_modif_max)
    for i in range(merch_more_or_less_number) :
        step = r.randint(0,l-1)
        merch = r.choice(list(actual_route[step]["merchandise"].keys()))
        more_or_less = r.choice([-1,1])
        actual_route[step]["merchandise"][merch] += r.randint(1,merch_modif_qty_max)*more_or_less
        if actual_route[step]["merchandise"][merch] <= 0:
            actual_route[step]["merchandise"][merch] = 0
    #adding or suppressing cities
    city_add_or_del_number = r.randint(city_add_or_del_min,city_add_or_del_max)
    for i in range(city_add_or_del_number) :
        l = len(actual_route)
        list_cities = []
        for j in actual_route :
            list_cities.append(j["from"])
        if actual_route != [] :
            list_cities.append(actual_route[-1]["to"])
        rd_city = r.choice(cities)
        number = r.random()
        if rd_city not in list_cities :
            if number < driver["agenda"]["pref_cities"][rd_city] :
                step = r.randint(-1,l)
                if actual_route == []:
                    rd_city2 = r.choice(cities)
                    if rd_city != rd_city2 :
                        actual_route.insert(0,{ "from" : rd_city, "to" : rd_city2, "merchandise" : {}})
                elif step == -1 :
                    actual_route.insert(0,{ "from" : rd_city, "to" : actual_route[0]["from"], "merchandise" : {}})
                elif step == l :
                    actual_route.append({ "from" : actual_route[l-1]["to"], "to" : rd_city, "merchandise" : {}})
                elif (rd_city != actual_route[step]["from"]) and (rd_city != actual_route[step]["to"]) :
                    temp = actual_route[step]["from"]
                    actual_route[step]["from"] = rd_city
                    actual_route.insert(step,{ "from" : temp, "to" : rd_city, "merchandise" : {}})
        elif actual_route != [] :
            step = r.randint(0,l-1)
            number = r.random()
            if step == -1 :
                if number > driver["agenda"]["pref_cities"][actual_route[0]["from"]] :
                    actual_route.pop(0)
            elif step == l-1 :
                if number > driver["agenda"]["pref_cities"][actual_route[l-1]["to"]] :
                    actual_route.pop(step)
            else :
                if number > driver["agenda"]["pref_cities"][actual_route[step]["to"]] :
                    actual_route[step+1]["from"] = actual_route[step]["from"]
                    actual_route.pop(step)
    #checking the association rules on merch
    for step in range(len(actual_route)) :
        for rule in driver["agenda"]["assoc_rules"]:
            merch_present = actual_route[step]["merchandise"].keys()
            if rule[0] in merch_present :
                if actual_route[step]["merchandise"][rule[0]] != 0 :
                    if rule[1] not in merch_present :
                        actual_route[step]["merchandise"][rule[1]] = r.randint(1,merch_add_max)
                    elif actual_route[step]["merchandise"][rule[1]] == 0 :
                        actual_route[step]["merchandise"][rule[1]] = r.randint(1,merch_add_max)
    return actual_route

#test
""" route = [{"from": "Perugia","to": "Potenza","merchandise": {"milk": 35,"coffee": 46,"honey": 25,}},
         {"from": "Potenza","to": "Verona","merchandise": {"salt": 2,"coca-cola": 34,"tomatoes": 49}}]

print(generate_actual_route(route,cities,merchandise_types)) """

# create a variation in the number of visited cities, of visited cities, of merchandise types, of merchandise quantities
# create an actual route based on a standard route, with a probability that gives which variations we apply
