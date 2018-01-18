'''
Given an array of ints, compute recursively if the array contains somewhere a
value followed in the array by that value times 10. We'll use the convention
of considering only the part of the array that begins at the given index. In
this way, a recursive call can pass index+1 to move down the array. The initial
call will pass in index as 0. 

array220({1, 2, 20}, 0) → true
array220({3, 30}, 0) → true
array220({3}, 0) → false
'''

def array220(nums,index):
    l = len(nums)
    if index==(l-1):
        return False
    else:
        k = nums[index]*10
        if k==nums[index+1]:
            return True
        else:
            return array220(nums,index+1)

n = input('Enter number of values: ')
print 'Enter %d array values: ' % (n)
lst = []
i=0
while i<n:
    k = input()
    lst.append(k)
    i+=1

print 'Does value followed by value*10 exist in this array?'
print 'Ans: ' + str(array220(lst,0))
        
