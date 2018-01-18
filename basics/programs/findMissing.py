'''
You are given a list of n-1 integers and these integers are in the range of 1
to n. There are no duplicates in list. One of the integers is missing in the
list. Write an efficient code to find the missing integer.
'''
#implementation-1
'''
def findMissing(lst,n):
    # using xor to find the missing number
    xall = 0
    xlst = 0
    for i in range(1,n+1):
        xall = xall^i

    for j in lst:
        xlst = xlst^j

    return xall^xlst  # this is the missing number
'''

#implementation-2
def findMissing(lst,n):
    # using sum operation
    slst = sum(lst)  # sum of all the number in the list lst
    sotn = sum(range(1,n+1)) # sum of numbers from 1 to n
    return sotn-slst


l = [1,2,4,6,3,7,8]
m = findMissing(l,8)
print 'Missing number in the list is: ' + `m`
    
