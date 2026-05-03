# Write your code here
import re

def remove_repeated_words(string):
    return re.sub(r'\b(\w+)( \1\b)+', r'\1', string)