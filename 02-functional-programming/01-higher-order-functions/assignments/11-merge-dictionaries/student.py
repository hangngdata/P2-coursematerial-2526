def merge_dictionaries(d1, d2, merge_function):
    merged_dict = {}
    for key in d1.keys() | d2.keys():
        if key in d1 and key in d2:
            merged_dict[key] = merge_function(d1[key], d2[key])
        elif key in d1:
            merged_dict[key] = d1[key]
        else:
            merged_dict[key] = d2[key]
            
    return merged_dict