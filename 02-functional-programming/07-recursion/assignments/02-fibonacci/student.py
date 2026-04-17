# Recursion
# def fibonacci(number):
#     if number <= 0:
#         return 0
#     if number == 1:
#         return 1
#     return fibonacci(number-2) + fibonacci(number-1)

# Iterative
def fibonacci(number):
    if number <= 0:
        return 0
    if number == 1:
        return 1

    n1, n2 = 0, 1
    sum = n1 + n2
    for _ in range(2, number):
        n1 = n2
        n2 = sum
        sum = n1 + n2
    return sum
    