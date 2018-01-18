'''
Given an array of ints, return the number of 9's in the array.

array_count9([1, 2, 9]) -> 1
array_count9([1, 9, 9]) -> 2
array_count9([1, 9, 9, 3, 9]) -> 3
'''

def array_count9(nums):
    n = 0
    for i in nums:
        if i==9:
            n+=1
    return n

print array_count9([1,2,9])
print array_count9([1,9,9])
print array_count9([1,9,9,3,9])
print array_count9([9,9,9,9,9])
