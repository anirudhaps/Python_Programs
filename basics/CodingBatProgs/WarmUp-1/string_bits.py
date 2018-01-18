'''
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

string_bits('Hello') -> 'Hlo'
string_bits('Hi') -> 'H'
string_bits('Heeololeo') -> 'Hello'
'''

import sys

def string_bits(dstr):
    l = len(dstr)
    out = ''
    i = 0
    while i<l:
        if i%2==0:
            out = out + dstr[i]
        i+=1
    return out
    
print string_bits(sys.argv[1])
