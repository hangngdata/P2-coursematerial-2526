from itertools import permutations, pairwise

def find_shortest_path(distance, city_count):
    best_path = None
    min_dist = float('inf')
    
    paths = permutations(range(1, city_count), city_count - 1)
    
    for p in paths:
        full_path = (0,) + p + (0,)
        current_dist = sum(distance(pair[0], pair[1]) for pair in pairwise(full_path))
        
        if current_dist < min_dist:
            min_dist = current_dist
            best_path = full_path
            
    return list(best_path)