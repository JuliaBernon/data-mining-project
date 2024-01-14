### Cities analysis ###
### This file contains functions and scripts to obtain the most frequent pairs of cities in the actual routes. ###

import json

with open("./data/actual.json") as actual_file:
    actual_routes = json.load(actual_file)


# function to transform a route into a list of pairs of cities
def route_to_pairs(route):
    '''
    Returns a list of pairs of cities from a route.

    Parameters:
    route (list[dict[str, str]]): A list of dictionaries representing the route, where each dictionary contains "from" and "to" keys.

    Returns:
    list[tuple[str, str]]: A list of pairs of cities from the route.
    '''
    pairs = []
    for i in range(len(route)):
        pairs.append((route[i]["from"], route[i]["to"]))
    return pairs

# store the pairs of cities of each actual route in a list
pairs_in_actual_routes = []
for route in actual_routes:
    pairs_in_actual_routes.append(route_to_pairs(route["route"]))
# print(pairs_in_actual_routes)

# create a function that returns the number of a pair of cities in the list of lists of pairs
def number_of_pair(pair, pairs):
    '''
    Returns the number of occurrences of a pair of cities in the list of lists of pairs.

    Parameters:
    pair : tuple(str, str) - The pair of cities to count.
    pairs : list(list(tuple(str, str))) - The list of lists of pairs.

    Returns:
    int - The number of occurrences of the pair in the list of lists of pairs.
    '''
    count = 0
    for route in pairs:
        if pair in route:
            count += 1
    return count

for pair_actual in pairs_in_actual_routes:
    pair_number = {}

    # iterate over each pair in pairs_in_actual_routes and update the number in pair_number
    for pair_actual in pairs_in_actual_routes:
        for pair in pair_actual:
            if pair in pair_number:
                pair_number[pair] += 1
            else:
                pair_number[pair] = 1
            
# create a function that computes the frequency of each pair
def compute_pair_frequency(pair, pairs):
    '''
    Computes the frequency of a pair based on the formula: frequency_of_a_pair = number_of_pair / total_number_of_pairs.
    pair : tuple(str, str)
    pairs : list(list(tuple(str, str)))
    '''
    total_pairs = sum(len(route) for route in pairs)
    pair_count = number_of_pair(pair, pairs)
    frequency = pair_count / total_pairs # compute the frequency of the pair
    return frequency

# # print the frequency for each pair
# for pair in sorted(pair_number, key=pair_number.get, reverse=True):
#     frequency = compute_pair_frequency(pair, pairs_in_actual_routes)
#     print(pair, " : ", frequency)

# create a function that returns the most frequent pairs of cities whose frequency is greater than or equal to a given threshold
def most_frequent_pairs(threshold):
    """
    Computes the frequency of each pair of cities in actual routes and returns the pairs
    that have a frequency greater than or equal to the given threshold.

    Args:
        threshold (int): The minimum frequency threshold for a pair to be included in the result.

    Returns:
        list: A list of pairs of cities that have a frequency greater than or equal to the threshold.
    """
    most_freq_pairs = []
    for pair in sorted(pair_number, key=pair_number.get, reverse=True):
        frequency = compute_pair_frequency(pair, pairs_in_actual_routes)
        if frequency >= threshold:
            most_freq_pairs.append(pair)
    return most_freq_pairs

## test
#print(most_frequent_pairs(0.005)) # threshold = 0.005
