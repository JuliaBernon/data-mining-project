import json

## Read and parse our data, created with dataGeneration.py

# Read and parse standard routes
with open("./data/standard.json", "r") as standard_file:
    standard_routes = json.load(standard_file)

# Read and parse actual routes
with open("./data/actual.json", "r") as actual_file:
    actual_routes = json.load(actual_file)