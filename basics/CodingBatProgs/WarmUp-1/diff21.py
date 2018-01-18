'''
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

diff21(19) -> 2
diff21(10) -> 11
diff21(21) -> 0
'''

import sys

def diff21(a):
    if a<=21:
        return 21-a
    else:
        return 2 * (a-21)

print diff21(int(sys.argv[1]))

