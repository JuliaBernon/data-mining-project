import random
import json

# read and parse cities.json
with open("./data/cities.json", "r") as cities_file:
    cities = json.load(cities_file)

# read and parse merchTypes.json
with open("./data/merchTypes.json", "r") as merchTypes_file:
    merchTypes = json.load(merchTypes_file)

# read and parse drivers.json
with open("./data/drivers.json", "r") as drivers_file:
    drivers = json.load(drivers_file)

# read and parse standard.json
with open("./data/standard.json", "r") as standard_file:
    standard_routes = json.load(standard_file)

## Generate actual routes for each driver and each standard routes

actual_routes = []
nb_actual_routes = 300 # define the number of actual routes
max_merch_quantity = 50 # max quantity for each merchType
merch_quantity_variation = 10 # small quantity of merch that the drivers add or omit

for driver in drivers :
    for standard_route_info in standard_routes:

        standard_route_id = standard_route_info["id"]
        standard_route = standard_route_info["route"]

        # create variations in merchandise quantities
        actual_merch = {}
        for merchType in merchTypes:
            if random.random() < 0.5: # 50% chance of creating no variation
                actual_merch[merchType] =  random.randint(1,max_merch_quantity)
            else: # 50% chance of creation variations
                std_merchQuantity = random.randint(1,max_merch_quantity)
                actual_merch[merchType] = std_merchQuantity + random.randint(-merch_quantity_variation, merch_quantity_variation)
                
        # Create variations in the route, adding/omitting cities
    actual_route = []
    from_city = random.choice(cities)
    to_city = random.choice(cities)
    while from_city == to_city:
        to_city = random.choice(cities)
    
    num_trips = random.randint(1, 5)  # Random number of trips (1 to 5)
    for _ in range(num_trips):
        merchandise = {item: actual_merch[item] for item in random.sample(merchTypes, random.randint(1, len(merchTypes)))}
        actual_route.append({"from": from_city, "to": to_city, "merchandise": merchandise})
        from_city = to_city
        to_city = random.choice(cities)
    
    # Add the actual route to the list
    actual_routes.append({
        "id": f"a{len(actual_routes) + 1}",
        "driver": driver,
        "sroute": standard_route_id,
        "route": actual_route
    })


# Save the synthetic actual routes to actual.json
with open("./data/actual.json", "w") as actual_file:
    json.dump(actual_routes, actual_file, indent=4)

