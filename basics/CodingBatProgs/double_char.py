'''
Given a string, return a string where for every char in the original, there are two chars.

double_char('The') -> 'TThhee'
double_char('AAbb') -> 'AAAAbbbb'
double_char('Hi-There') -> 'HHii--TThheerree'
'''

import sys

def double_char(dstr):
    r = ''
    for c in dstr:
        r = r + 2*c
    return r
    
print double_char(sys.argv[1])

