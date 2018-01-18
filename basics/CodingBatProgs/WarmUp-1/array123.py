'''
Given an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere.

array123([1, 1, 2, 3, 1]) -> True
array123([1, 1, 2, 4, 1]) -> False
array123([1, 1, 2, 1, 2, 3]) -> True
'''

def array123(nums):
    s = ''.join(str(e) for e in [1,2,3])  #converting a list into string: output: '123'
    numstr = ''.join(str(e) for e in nums) #converting nums into string
    return s in numstr
    
print array123([1,1,2,3,1])
print array123([1,1,2,4,1])
print array123([1,1,2,1,2,3])
