from itertools import groupby

def rle_encode(data):
    data = list(data)
    
    if not data:
        return []

    summary = []
    count = 1
    
    previous = data[0]

    for char in data[1:]:
        if char == previous:
            count += 1
        else:
            summary.append((previous, count))
            previous = char
            count = 1
    summary.append((previous, count))
    
    return summary

def rle_decode(data):
    string = ""
    for char, count in data:
        sub = char * count
        string += sub
    return string