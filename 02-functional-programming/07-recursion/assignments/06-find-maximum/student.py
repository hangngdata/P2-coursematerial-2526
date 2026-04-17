def findMaximum(list):
    if len(list) == 0:
        raise IndexError
    
    if len(list) == 1:
        return list[0]
    
    return max(list[0], findMaximum(list[1:]))