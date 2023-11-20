### This file contains a function to generate a new standard route, given a set of pairs of cities and merchandise types ###

import random
import json

# function to generate a new standard route
def generate_new_route(pairs_of_cities, merchandise_types):
    '''
    Generate a new standard route, given a set of pairs of cities and merchandise types

    pairs_of_cities : List[(str, str)]
    merchandise_types : List[str]

    generate_new_route(pairs_of_cities, merchandise_types) -> List[Dict[str, Any]]
    '''
    route = []
    from_city, to_city = random.choice(pairs_of_cities)
    num_trips = random.randint(1, 5)  # number of trips (1 to 5)
    for _ in range(num_trips):
        # random number of merchandise types with maximum 50 items of each type
        # merchandise = {item: random.randint(1, 50) for item in random.sample(merchandise_types, random.randint(1, len(merchandise_types)))}
        merchandise = {item: random.randint(1, 50) for item in random.sample(list(merchandise_types), random.randint(1, len(merchandise_types)))}
        route.append({"from": from_city, "to": to_city, "merchandise": merchandise})
        from_city = to_city
        to_city = random.choice(pairs_of_cities)[1] # next city is the second city of a random pair of cities
    return route
