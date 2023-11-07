import json
import random

cities = ["Rome", "Milan", "Verona", "Venezia", "Bergamo", "Bolzano", "Trento"]
merchandise_types = ["milk", "honey", "butter", "tomatoes", "pens", "bread", "coca-cola"]

## Generate our data for actual and standard routes

# Generate standard routes
standard_routes = []
nb_standard_routes = 10 # define the number of standard routes
nb_trip_per_standard_route = random.randint(1,5) # define the number of trips per standard route

for i in range(nb_standard_routes):
    route_id = f"s{i+1}"
    route = []
    from_city = random.choice(cities)
    to_city = random.choice(cities)
    while from_city == to_city:
        to_city = random.choice(cities)
    
    for j in range(nb_trip_per_standard_route):
        merchandise = {item: random.randint(1, 50) for item in random.sample(merchandise_types, random.randint(1, len(merchandise_types)))}
        route.append({"from": from_city, "to": to_city, "merchandise": merchandise})
        from_city = to_city
        to_city = random.choice(cities)
    
    standard_routes.append({"id": route_id, "route": route})

# save data into standard.json
with open("./data/standard.json", "w") as standard_file:
    json.dump(standard_routes, standard_file, indent=4)

# Generate actual routes
actual_routes = []
nb_actual_routes = 10 # define the number of actual routes
nb_trip_per_actual_route = random.randint(1,5) # define the number of trips per actual route

# Define the drivers
drivers = ["A", "B", "C", "D", "E"]
nb_drivers = len(drivers)

for i in range(nb_actual_routes):
    route_id = f"a{i+1}"
    driver = random.choice(drivers)
    standard_route = f"s{i+1}"
    route = []
    from_city = random.choice(cities)
    to_city = random.choice(cities)
    while from_city == to_city:
        to_city = random.choice(cities)
    
    for j in range(nb_trip_per_actual_route):
        merchandise = {item: random.randint(1, 50) for item in random.sample(merchandise_types, random.randint(1, len(merchandise_types)))}
        route.append({"from": from_city, "to": to_city, "merchandise": merchandise})
        from_city = to_city
        to_city = random.choice(cities)
    
    actual_routes.append({"id": route_id, "driver": driver, "sroute": standard_route, "route": route})

# save data into actual.json
with open("./data/actual.json", "w") as actual_file:
    json.dump(actual_routes, actual_file, indent=4)


## Read and parse our data

# Read and parse standard routes
with open("./data/standard.json", "r") as standard_file:
    standard_routes = json.load(standard_file)

# Read and parse actual routes
