'''
Given an array of ints, compute recursively if the array contains a 6. We'll
use the convention of considering only the part of the array that begins at
the given index. In this way, a recursive call can pass index+1 to move down
the array. The initial call will pass in index as 0. 

array6({1, 6, 4}, 0) → true
array6({1, 4}, 0) → false
array6({6}, 0) → true
'''

def array6(nums,index):
    l = len(nums)
    if index==l:
        return False
    else:
        if nums[index]==6:
            return True
        else:
            return array6(nums,index+1)


n = input('Enter number of values: ')
print 'Enter %d array values: ' % (n)
lst = []
i=0
while i<n:
    k = input()
    lst.append(k)
    i+=1

if array6(lst,0)==True:
    print 'Output: 6 is present in it'
else:
    print 'Output: 6 is not present in it'

