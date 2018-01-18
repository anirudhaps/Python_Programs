'''
Given an array of ints, compute recursively the number of times that the value
11 appears in the array. We'll use the convention of considering only the part
of the array that begins at the given index. In this way, a recursive call can
pass index+1 to move down the array. The initial call will pass in index as 0. 

array11({1, 2, 11}, 0) → 1
array11({11, 11}, 0) → 2
array11({1, 2, 3, 4}, 0) → 0
'''

def array11(nums,index):
    l = len(nums)
    if index==l:
        return 0
    else:
        if nums[index]==11:
            return 1 + array11(nums,index+1)
        else:
            return array11(nums,index+1)

n = input('Enter number of values: ')
print 'Enter %d array values: ' % (n)
lst = []
i=0
while i<n:
    k = input()
    lst.append(k)
    i+=1

print 'Number of 11\'s in the array is ' + str(array11(lst,0))
