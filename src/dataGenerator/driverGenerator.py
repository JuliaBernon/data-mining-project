### This file contains scripts to create driver agenda ###

# function to generate a driver

import random

def set_tendancy(pref_merch):
    '''
    Return a dictionary of merchandise types and the driver's tendancy to get more or less of each type
    
    pref_merch : Dict[str, float]

    set_tendancy(pref_merch) -> Dict[str, int]
    '''
    merch_tendancy = {}
    for merch in pref_merch:
        if pref_merch[merch] <= 0.5:
            merch_tendancy[merch] = -1
        elif pref_merch[merch] > 0.5 and pref_merch[merch] <= 0.8:
            merch_tendancy[merch] = 0
        else:
            merch_tendancy[merch] = 1
    return merch_tendancy

def generate_driver(cities, merchandise_types):

    '''
    Generate a driver, given a set of cities and merchandise types
    
    cities : List[str]
    merchandise_types : List[str]

    generate_driver(cities, merchandise_types) -> Dict[str, Any]
    '''

    driver = {}
    driver["pref_cities"] = {city: random.random() for city in cities}
    driver["pref_merch"] = {item: random.random() for item in merchandise_types}
    #driver["tendancy"] = set_tendancy(driver["pref_merch"])
    #driver["amp_tendancy"] = random.randint(1, 10)
    driver["assoc_rules"] = [random.sample(merchandise_types,2) for i in range(2)]
    
    return driver
