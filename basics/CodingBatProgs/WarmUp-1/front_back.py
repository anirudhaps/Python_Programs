'''
Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') -> 'eodc'
front_back('a') -> 'a'
front_back('ab') -> 'ba'
'''
import sys

def front_back(str):
    if len(str)==0 or len(str)==1:
        return str
    elif len(str)==2:
        return str[1] + str[0]
    else:
        return str[-1] + str[1:len(str)-1] + str[0]
        
print front_back(sys.argv[1])
