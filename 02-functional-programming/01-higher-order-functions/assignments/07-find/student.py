def find(object_list, condition_function):
    for object in object_list:
        if condition_function(object):
              return object
    return None

def has_consecutive_characters(string):
    for index in range(len(string) - 1):
        if string[index] == string[index + 1]:
                    return string
        
print(find(["monkey", "banana", "computer", "yellow", "oddish"], has_consecutive_characters))