'''
Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

missing_char('kitten', 1) -> 'ktten'
missing_char('kitten', 0) -> 'itten'
missing_char('kitten', 4) -> 'kittn'
'''

import sys

def missing_char(dstr,n):
    if n<0 or n>=len(dstr):
        print 'invalid index n'
    else:
        if n==0:
            return dstr[1:]
        else:
            return dstr[0:n] + dstr[n+1:]


val = missing_char(sys.argv[1],int(sys.argv[2]))
if val!=None:
    print val
