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
def generate_actual_route(standard_route, cities, merchandise_types):

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
        if merch in actual_route[step]["merchandise"].keys():
            actual_route[step]["merchandise"][merch] = 0
        else :
            actual_route[step]["merchandise"][merch] = r.randint(1,merch_add_max)
    #transporting a little more or a little less merchandise
    merch_more_or_less_number = r.randint(merch_modif_min,merch_modif_max)
    for i in range(merch_more_or_less_number) :
        step = r.randint(0,l-1)
        merch = r.choice(list(actual_route[step]["merchandise"].keys()))
        more_or_less = r.choice([-1,1])
        actual_route[step]["merchandise"][merch] += r.randint(1,merch_modif_qty_max)*more_or_less
    #adding or suppressing cities
    city_add_or_del_number = r.randint(city_add_or_del_min,city_add_or_del_max)
    for i in range(city_add_or_del_number) :
        l = len(actual_route)
        add_or_del = r.randint(0,1)
        if add_or_del :
            step = r.randint(-1,l)
            city_add = r.choice(cities)
            if actual_route == []:
                city_add2 = r.choice(cities)
                if city_add != city_add2 :
                    actual_route.insert(0,{ "from" : city_add, "to" : city_add2, "merchandise" : {}})
            elif step == -1 :
                actual_route.insert(0,{ "from" : city_add, "to" : actual_route[0]["from"], "merchandise" : {}})
            elif step == l :
                actual_route.append({ "from" : actual_route[l-1]["to"], "to" : city_add, "merchandise" : {}})
            elif (city_add != actual_route[step]["from"]) and (city_add != actual_route[step]["to"]) :
                temp = actual_route[step]["from"]
                actual_route[step]["from"] = city_add
                actual_route.insert(step,{ "from" : temp, "to" : city_add, "merchandise" : {}})
        elif actual_route != [] :
            step = r.randint(0,l-1)
            if step == -1 :
                actual_route.pop(0)
            elif step == l-1 :
                actual_route.pop(step)
            else :
                actual_route[step+1]["from"] = actual_route[step]["from"]
                actual_route.pop(step)
    return actual_route

#test
""" route = [{"from": "Perugia","to": "Potenza","merchandise": {"milk": 35,"coffee": 46,"honey": 25,}},
         {"from": "Potenza","to": "Verona","merchandise": {"salt": 2,"coca-cola": 34,"tomatoes": 49}}]

print(generate_actual_route(route,cities,merchandise_types)) """

# create a variation in the number of visited cities, of visited cities, of merchandise types, of merchandise quantities
# create an actual route based on a standard route, with a probability that gives which variations we apply
