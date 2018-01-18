'''
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

not_string('candy') -> 'not candy'
not_string('x') -> 'not x'
not_string('not bad') -> 'not bad'
'''
import sys

def not_string(gstr):
    if gstr[0:3]=='not':
        return gstr
    else:
        return 'not ' + gstr

print not_string(sys.argv[1])
