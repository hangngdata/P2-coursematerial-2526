import re

def parse_time(string):
    match = re.fullmatch(r'^\d{2}:\d{2}:\d{2}(?:\.(\d{3}))?$', string)

    if not match:
        return None
    
    parts = string.replace('.', ':').split(':')
    h, m, s = int(parts[0]), int(parts[1]), int(parts[2])
    ms = int(parts[3]) if len(parts) == 4 else 0
    
    if m > 59 or s > 59:
        return None
    
    return (h, m, s, ms)
        
