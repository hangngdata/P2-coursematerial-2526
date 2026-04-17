import re

def sum_numbers(number):
    if number < 0:
        number = -number
    if number == 0:
        return 0
    number, remainder = divmod(number, 10)
    return remainder + sum_numbers(number)