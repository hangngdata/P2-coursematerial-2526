# Write your code here
import re

def remove_trailing_whitespace(string, flag=re.MULTILINE):
    return re.sub(r'\s+$', '', string, flags=flag)