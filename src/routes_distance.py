### Compute the distance between two routes ###

from lev_distance import levenshtein_distance_list
from flatten_json import flatten_json
import json

with open("./data/actual.json", "r") as actual_file:
    actual_routes = json.load(actual_file)

with open("./results/recStandard.json", "r") as recstd_file:
    recstd_routes = json.load(recstd_file)

def compute_distance(actual_route, recstd_route):
    '''
    Compute the distance between two routes.
    actual_route : Dict[str, Any]
    std_route : Dict[str, Any]
    '''
    # flatten the routes
    actual_route_flattened = flatten_json(actual_route)
    std_route_flattened = flatten_json(recstd_route)

    # compute the distance between the two routes
    distance = levenshtein_distance_list(actual_route_flattened, std_route_flattened)

    return distance

# test
print(compute_distance(actual_routes[0], recstd_routes[0]))
