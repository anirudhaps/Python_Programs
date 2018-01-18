'''
Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().

no_teen_sum(1, 2, 3) -> 6
no_teen_sum(2, 13, 1) -> 3
no_teen_sum(2, 1, 14) -> 3
'''

from sys import argv

def no_teen_sum(a,b,c):
    teens = range(13,20)
    teens.remove(15)
    teens.remove(16)
    #print teens
    s=0
    if a not in teens:
        s+=a
    if b not in teens:
        s+=b
    if c not in teens:
        s+=c
    return s
    
va = int(argv[1])
vb = int(argv[2])
vc = int(argv[3])
print no_teen_sum(va,vb,vc)
