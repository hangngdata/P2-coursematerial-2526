def indices_of(ls, condidtion):
    indices_list = []
    for i in range(len(ls)):
        if condidtion(ls[i]):
            indices_list.append(i)
    return indices_list

def is_palindrome(string):
    return string == string[::-1]

print(indices_of(["kayak", "never", "rotator", "palindrome"], is_palindrome))