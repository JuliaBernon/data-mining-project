### Flatten JSON ###

# This function takes a JSON object and flattens it into a list of strings.
def flatten_json(json_obj, separator='_'):
    """
    Flattens a JSON object by converting nested keys into a flat structure.

    Args:
        json_obj (dict or list): The JSON object to be flattened.
        separator (str, optional): The separator to be used between keys in the flattened structure. 
            Defaults to '_'.

    Returns:
        list: A list containing the flattened keys and values from the JSON object.
    """
    result = []

    def flatten_helper(obj, path=''):
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_path = f"{path}{separator}{key}" if path else key
                if key == 'merchandise' and isinstance(value, dict):
                    for merch_key, merch_value in sorted(value.items()):
                        merchandise_key = str(merch_key)
                        merchandise_value = str(merch_value)
                        result.append(merchandise_key)
                        result.append(merchandise_value)
                else:
                    flatten_helper(value, new_path)
        elif isinstance(obj, list):
            for i, value in enumerate(obj):
                new_path = f"{path}{separator}{i}" if path else str(i)
                flatten_helper(value, new_path)
        else:
            result.append(str(obj))

    flatten_helper(json_obj)
    return result

# # test
# import json
# with open("./data/actual.json") as actual_file:
#     actual_routes = json.load(actual_file)
# print(flatten_json(actual_routes[0]))

