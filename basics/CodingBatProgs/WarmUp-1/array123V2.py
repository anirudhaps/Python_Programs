'''
Given an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere.

array123([1, 1, 2, 3, 1]) -> True
array123([1, 1, 2, 4, 1]) -> False
array123([1, 1, 2, 1, 2, 3]) -> True
'''

def array123V2(nums):
    l = [1,2,3]
    i=0
    while i<len(nums):
        slc = nums[i:i+3]
        if slc==l:
            return True
        i+=1
    return False
    
print array123V2([1,1,2,3,1])
print array123V2([1,1,2,4,1])
print array123V2([1,1,2,1,2,3])
