### This file contains a function to generate a new standard route, given a set of pairs of cities and merchandise types ###

import random

# function to generate a new standard route
def generate_new_route(pairs_of_cities, merchandise_types):
    '''
    Generate a new standard route, given a set of pairs of cities and merchandise types

    pairs_of_cities : List[(str, str)]
    merchandise_types : List[List[str]]

    generate_new_route(pairs_of_cities, merchandise_types) -> List[Dict[str, Any]]
    '''
    # pairs_of_cities = [(city1, city2), (city3, city4), ...]
    # merchandise_types = ['[item1]', '[item3, item4, ...]', ...]
    route = []
    from_city, to_city = random.choice(pairs_of_cities)
    num_trips = random.randint(1, 5)  # number of trips (1 to 5)
    for _ in range(num_trips):
        # generate a new trip
        selected_merchandise = random.choice(merchandise_types)
        items = selected_merchandise[1:-1].split(", ")
        trip = {
            "from": from_city,
            "to": to_city,
            "merchandise": {item: random.randint(1,50) for item in items}
        }
        route.append(trip)
        # generate a new pair of cities
        # from_city, to_city = random.choice(pairs_of_cities)
        city_list = [city for city in pairs_of_cities if city[0] == to_city]
        if city_list:

            from_city, to_city = random.choice(city_list)
        else:
            # in that case, we have reached the end of the route
            break
    return route

# # test
# pairs_of_cities = [("New York", "Los Angeles"), ("Chicago", "Houston"), ("Phoenix", "Philadelphia")]
# merchandise_types = [["books", "clothes"], ["electronics"], ["groceries", "furniture"]]

# route = generate_new_route(pairs_of_cities, merchandise_types)
# print(route)
