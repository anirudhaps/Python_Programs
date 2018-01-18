'''
Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.

close_far(1, 2, 10) -> True
close_far(1, 2, 3) -> False
close_far(4, 1, 3) -> True
'''
from sys import argv

def close_far(a,b,c):
    dab = abs(a-b)
    dac = abs(a-c)
    dbc = abs(b-c)       
    if dab<=1:        
        cval = b
    elif dac<=1:
        cval = c
    else:
        return False
    
    if cval==b:
        if dac>=2 and dbc>=2:
            return True
        else:
            return False
    else:
        if dab>=2 and dbc>=2:
            return True
        else:
            return False

va = int(argv[1])
vb = int(argv[2])
vc = int(argv[3])
print close_far(va,vb,vc)
