def flatten_json(json_obj, separator='_'):
    result = []

    def flatten_helper(obj, path=''):
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_path = f"{path}{separator}{key}" if path else key
                if key == 'merchandise' and isinstance(value, dict):
                    for merch_key, merch_value in value.items():
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

