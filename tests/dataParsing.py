### This file is used to print all the data in a readable format ###

import json

## Read and parse our data, created with dataGeneration.py

# Read and parse standard routes
with open("./data/standard.json", "r") as standard_file:
    standard_routes = json.load(standard_file)

# Read and parse actual routes
with open("./data/actual.json", "r") as actual_file:
    actual_routes = json.load(actual_file)

# Read and parse drivers
with open("./data/drivers.json", "r") as drivers_file:
    drivers = json.load(drivers_file)

## Print data

# print standard routes
print("Standard routes :")
for route in standard_routes:
    print(f"Route {route['id']}:")
    for step in route["route"]:
        print(f"\tFrom {step['from']} to {step['to']} with {step['merchandise']}")
    print("\n")


# print actual routes
print("Actual routes :")
for route in actual_routes:
    print(f"Route {route['id']} (driver {route['driver']}) associated to standard route {route['sroute']}:")
    for step in route["route"]:
        print(f"\tFrom {step['from']} to {step['to']} with {step['merchandise']}")
    print("\n")

## Print, for each standard route, the associated actual routes
print("Standard routes and associated actual routes :")
for route in standard_routes:
    print(f"Standard route {route['id']} :")
    for actual_route in actual_routes:
        if actual_route["sroute"] == route["id"]:
            print(f"\tActual route {actual_route['id']} (driver {actual_route['driver']})")
    print("\n")

## Print, for each driver, the associated standard routes and actual routes, with the format : "Driver X : S1 [A1, A2,...], S2 [A3, A4,...],..."
print("Drivers and associated actual routes :")
for driver in drivers:
    print(f"Driver {driver} :")
    for route in standard_routes:
        if route["id"] in [actual_route["sroute"] for actual_route in actual_routes if actual_route["driver"] == driver]:
            print(f"\t{route['id']} : {[actual_route['id'] for actual_route in actual_routes if actual_route['sroute'] == route['id'] and actual_route['driver'] == driver]}")
    print("\n")



