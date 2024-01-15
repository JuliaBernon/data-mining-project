## This file contains functions to test if we can identify the mainRules in our actual routes
# based on 500 standard routes and 20000 actual routes
# we compare the data to those that are in ./data/mainRules_example.json file that is provided
import json
from collections import Counter
import matplotlib.pyplot as plt

# read and parse actual routes
actual_file = 'actual.json'
with open(f"./data/{actual_file}", 'r') as f:
    actual = json.load(f)

# function to transform a route into a list of pairs of cities
def routes_to_cities(routes):
    """
    Extracts the cities from a list of routes.

    Args:
        routes (list): A list of routes, where each route is a dictionary.

    Returns:
        list: A list of cities extracted from the routes.
    """
    cities = []
    for route in routes:
        for i in range(len(route['route'])):
            cities.append(route['route'][i]['from'])
            cities.append(route['route'][i]['to'])
    return cities

cities_in_actual_routes = routes_to_cities(actual)
# print(cities_in_actual_routes)

def most_frequent_cities(cities, nb_most_frequent):
    '''
    Returns the most frequent cities in a list of cities.

    Parameters:
    cities (list[str]): A list of cities.
    nb_most_frequent (int): The number of most frequent cities to return.

    Returns:
    list[str]: A list of the most frequent cities in the list of cities.
    '''
    city_count = Counter(cities)  
    most_frequent = city_count.most_common(nb_most_frequent)
    return most_frequent


def route_to_merchandises(route):
    """
    Extracts the merchandise from each step in the given route.
    Args:
        route (list): A list of dictionaries representing the route.
    Returns:
        list: A list of merchandise extracted from each step in the route.
    """
    merchandises = []
    for step in route:
        merchandises.append(step["merchandise"])
    return merchandises

def route_to_list_merch(route):
    """
    Converts a route to a list of merchandise types.
    Parameters:
    route (list): A list of dictionaries representing the route.
    Returns:
    list: A list of merchandise types extracted from the route.
    """
    route_merchandise_types = []
    for dictionary in route_to_merchandises(route):
        merchandise_types = list(dictionary.keys())
        route_merchandise_types.append(merchandise_types)
    return route_merchandise_types

all_merchandise_types = [merch for route in actual for merch in route_to_list_merch(route["route"])]
flat_merchandise_types = [merch_type for sublist in all_merchandise_types for merch_type in sublist]

def most_frequent_merchandises(merchandises, nb_most_frequent):
    '''
    Returns the most frequent merchandise types in a list of merchandise types.

    Parameters:
    merchandises (list[str]): A list of merchandise types.
    nb_most_frequent (int): The number of most frequent merchandise types to return.

    Returns:
    list[str]: A list of the most frequent merchandise types in the list of merchandise types.
    '''
    merchandise_count = Counter(merchandises)  
    most_frequent = merchandise_count.most_common(nb_most_frequent)
    return most_frequent


## Check correlation between mainRules and actual routes
# check best and worst cities
most_frequent = most_frequent_cities(cities_in_actual_routes, 20)
print(most_frequent)

# check best and worst merchandise types
most_frequent_merch = most_frequent_merchandises(flat_merchandise_types, 92)
print(most_frequent_merch)

# plot histograms
def plot_histogram(data, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    plt.bar(*zip(*data), color='skyblue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

plot_histogram(
    most_frequent,
    title="City Occurrences",
    xlabel="Cities",
    ylabel="Occurrences"
)

plot_histogram(
    most_frequent_merch,
    title="Merchandise Occurrences",
    xlabel="Merchandise",
    ylabel="Occurrences"
)
