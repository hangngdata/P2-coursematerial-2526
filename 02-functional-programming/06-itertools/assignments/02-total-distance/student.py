from itertools import pairwise

def total_distance(path, distance):
        return sum(distance(pair[0], pair[1]) for pair in pairwise(path))
