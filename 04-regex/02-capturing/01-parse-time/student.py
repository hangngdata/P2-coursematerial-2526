import re

def parse_time(string):
    match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(.\d{3}|:\d{3})?', string)

    if match:
        return match.groups('')
    else:
        return None
