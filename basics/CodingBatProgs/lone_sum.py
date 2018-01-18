'''
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.

lone_sum(1, 2, 3) -> 6
lone_sum(3, 2, 3) -> 2
lone_sum(3, 3, 3) -> 0
'''

from sys import argv

def lone_sum(a,b,c):
    l = [b] + [c]
    #print l
    s = 0
    if a not in l:
        s+=a
    l.append(a)
    del l[0]
    #print l
    if b not in l:
        s+=b
    l.append(b)
    del l[0]
    #print l
    if c not in l:
        s+=c
    return s
    
va = int(argv[1])
vb = int(argv[2])
vc = int(argv[3])
print lone_sum(va,vb,vc)
