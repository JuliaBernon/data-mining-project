import random
import json

# read and parse cities.json
with open("./data/cities.json", "r") as cities_file:
    cities = json.load(cities_file)

# read and parse merchTypes.json
with open("./data/merchTypes.json", "r") as merchTypes_file:
    merchTypes = json.load(merchTypes_file)

## Generate standard routes

standard_routes = []
nb_standard_routes = 300 # define the number of standard routes
# nb_steps_per_standard_route = random.randint(1,5) # define the number of steps per standard route

for i in range(nb_standard_routes):
    route_id = f"s{i+1}"
    route = []
    from_city = random.choice(cities)
    to_city = random.choice(cities)
    
    while from_city == to_city: # make sure that the from and to cities are different
        to_city = random.choice(cities)
    
    for j in range(random.randint(0,5)): # define the number of steps per standard route

        # define the merchandise for each step, with a maximum of 50 items per merchandise type
        merchandise = {item: random.randint(1, 50) for item in random.sample(merchTypes, random.randint(1, len(merchTypes)))} 

        # add the step to the route
        route.append({"from": from_city, "to": to_city, "merchandise": merchandise})
        from_city = to_city
        to_city = random.choice(cities)
    
    standard_routes.append({"id": route_id, "route": route})

# save data into standard.json
with open("./data/standard.json", "w") as standard_file:
    json.dump(standard_routes, standard_file, indent=4)


