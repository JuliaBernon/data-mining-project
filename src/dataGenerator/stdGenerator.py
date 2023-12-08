### This file contains a function to generate a standard route, given a set of cities and merchandise types ###

import random

# function to generate a standard route
def generate_route(cities, merchandise_types):

    '''
    Generate a standard route, given a set of cities and merchandise types
    
    cities : List[str]
    merchandise_types : List[str]

    generate_route(cities, merchandise_types) -> List[Dict[str, Any]]
    '''

    route = []
    from_city = random.choice(cities)
    to_city = random.choice(cities)
    while from_city == to_city:
        to_city = random.choice(cities)
    
    num_trips = random.randint(1, 5)  # number of trips (1 to 5)
    for _ in range(num_trips):
        # random number of merchandise types with maximum 50 items of each type
        #merchandise = {item: random.randint(1, 50) for item in random.sample(merchandise_types, random.randint(1, len(merchandise_types)))}
        merchandise = {item: random.randint(1, 50) for item in random.sample(merchandise_types, random.randint(1, 10))}
        route.append({"from": from_city, "to": to_city, "merchandise": merchandise})
        from_city = to_city
        to_city = random.choice(cities)
    return route