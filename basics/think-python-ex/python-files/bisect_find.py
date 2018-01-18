'''
Exercise 10-11
'''

import bisect
import time
from build_list import build_list_V1

def bisect_find_V1(a,x):
    i = bisect.bisect(a,x)
    if a[i-1]==x:
        return i-1
    else:
        return None

def bisect_find_V2(a,x):
    if x in a:
        return a.index(x)
    else:
        return None

def bisect_find_V3(a,x):
    start = 0
    end = len(a)-1
    while start<=end:
        mid = (start + end)/2
        if x==a[mid]:
            return mid
        elif x<a[mid]:
            end = mid-1
        else:
            start = mid+1
    return None

lst = build_list_V1()
#print lst
x = raw_input('Enter the element to be searched: ')
start = time.time()
print bisect_find_V1(lst,x)
elapsed_time = time.time() - start
print 'elapsed time for V1: ' + str(elapsed_time) 

start = time.time()
print bisect_find_V2(lst,x)
elapsed_time = time.time() - start
print 'elapsed time for V2: ' + str(elapsed_time) 

start = time.time()
print bisect_find_V3(lst,x)
elapsed_time = time.time() - start
print 'elapsed time for V3: ' + str(elapsed_time) 
