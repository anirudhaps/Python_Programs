'''
Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.

big_diff([10, 3, 5, 6]) -> 7
big_diff([7, 2, 10, 9]) -> 8
big_diff([2, 10, 7, 2]) -> 8
'''

def big_diff(lst):    
    i = 1
    mi = lst[0]
    ma = lst[0]
    while i<len(lst):
        mi = min(mi,lst[i])
        ma = max(ma,lst[i])
        i+=1
    return ma-mi

print big_diff([10,3,5,6])
print big_diff([7,2,10,9])
print big_diff([2,10,7,2])
