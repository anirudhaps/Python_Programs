'''
Exercise 10-8-1
'''
from has_duplicates_v2 import has_duplicates_v2
from time import time

def has_duplicates(lst):
    i=0
    while i<len(lst)-1:
        if lst[i] in lst[i+1:]:
            return True
        i+=1
    return False

n = int(raw_input('n = '))
l = []
print 'Enter '+ `n` +' numbers:'
for i in range(n):
    v = int(raw_input())
    l.append(v)

st = time()
print has_duplicates(l)
et = time() - st
print 'time for v1: ' + `et`

st = time()
print has_duplicates_v2(l)
et = time() - st
print 'time for v1: ' + `et`
