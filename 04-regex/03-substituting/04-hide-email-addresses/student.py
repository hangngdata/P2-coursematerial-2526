# Write your code here
import re

def hide_email_addresses(string):
    def replace(match):
        matched = match.group()
        return '*' * len(matched)

    return re.sub(r'[a-z0-9.]+@[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)+', replace, string)