from collections import Counter

def is_sorted(ns):
    return all(ns[i] < ns[i+1] for i in range(len(ns)-1))

def contain_same_elements(xs, ys): # checked solution: need to also check if the two sequences have the same elements
    return Counter(xs) == Counter(ys)


def split_in_two(ns):
    middle = len(ns) // 2
    left = ns[:middle]
    right = ns[middle:]
    assert all(x in ns for x in left)
    assert all(x in ns for x in right)
    assert left + right == ns
    assert abs(len(left)  - len(right)) <= 1 # checked solution: need to check of the len of the two half is at most 1
    return (left, right)

def merge_sorted(ks, ns):
    assert is_sorted(ks) # checked solution: need to check if the sequences are sorted before merge, else it is expensive to perform in release builds
    assert is_sorted(ns)

    result = []
    i = 0
    j = 0
    while i < len(ks) and j < len(ns):
        if ks[i] < ns[j]:
            result.append(ks[i])
            i += 1
        else:
            result.append(ns[j])
            j += 1
    result.extend(ks[i:])
    result.extend(ns[j:])

    assert is_sorted(result)
    assert contain_same_elements(ks + ns, result) # checked solutions
    return result


def merge_sort(ns):
    if len(ns) <= 1:
        result = ns
    else:
        left, right = split_in_two(ns)
        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)
        result = merge_sorted(sorted_left, sorted_right)
    assert is_sorted(result)
    assert contain_same_elements(result, ns) # checked solutions
    return result
