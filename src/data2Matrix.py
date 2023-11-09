import json

# Read and parse standard routes
with open("./data/standard.json", "r") as standard_file:
    standard_routes = json.load(standard_file)

# Read and parse actual routes
with open("./data/actual.json", "r") as actual_file:
    actual_routes = json.load(actual_file)

# Read and parse drivers
with open("./data/drivers.json", "r") as drivers_file:
    drivers = json.load(drivers_file)

# Read and parse cities
with open("./data/cities.json", "r") as cities_file:
    cities = json.load(cities_file)

# Read and parse merchTypes
with open("./data/merchTypes.json", "r") as merchTypes_file:
    merchTypes = json.load(merchTypes_file)

def routeToMatrix(route, elts):
    '''
    Convert a route to a matrix
    route : List[Dict[str, Any]]
    elts : List[Any]
    routeToMatrix(route, elts) -> List[List[int]]
    '''
    matrix = []
    for step in route:
        matrix.append([1 if elt in step["merchandise"] else 0 for elt in elts])
    return matrix