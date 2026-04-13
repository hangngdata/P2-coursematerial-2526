def group_by(xs, key_function):
    result_dict = {}
    for item in xs:
        dict_key = key_function(item)
        if dict_key not in result_dict:
            result_dict[dict_key] = [item]
        else: 
            result_dict[dict_key].append(item)
    return result_dict