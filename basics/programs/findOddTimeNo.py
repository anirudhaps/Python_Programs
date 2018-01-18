'''
Given an array of positive integers. All numbers occur even number of times
except one number which occurs odd number of times. Find the number in O(n)
time & constant space.
'''

def findOddTimeNo(arr):
    #x = 0
    #for i in arr:
        #x = x^i  # performing xor of all the elements in the list arr
    # alternative implementation:
    x = reduce(lambda k,l: k^l, arr)
    print 'The only number that is occuring odd number of times is: ' + `x`

lst = [1,2,3,2,3,1,3]
findOddTimeNo(lst)
lst = [2,3,5,4,5,2,4,3,5,2,4,4,2]
findOddTimeNo(lst)
