def linear_search(students, target_id):
    if len(students) == 0:
        return None

    for student in students:
        if student.id  == target_id:
            return student
        
    return None

def binary_search(students, target_id):
    if len(students) == 0:
        return None
    
    left = 0
    right = len(students) - 1

    while left <= right:
        middle = (right + left) // 2

        if students[middle].id == target_id:
            return students[middle]
        elif target_id < students[middle].id:
            right = middle - 1
        else: 
            left = middle + 1
    return None
    
    


