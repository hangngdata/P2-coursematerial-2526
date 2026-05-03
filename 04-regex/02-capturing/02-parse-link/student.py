# Write your code here
import re

def parse_link(string):
    pattern = r'<a href="(.+)">(.+)</a>'
    match = re.fullmatch(pattern, string)

    if not match:
        return None
    
    return (str(match.group(2)), str(match.group(1)))
