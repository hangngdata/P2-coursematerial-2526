# Write your code here
import re
def ababa(string):
    return re.fullmatch(r'(.)(\1*)(.)(\3*)\1\2\3\4\1\2', string)