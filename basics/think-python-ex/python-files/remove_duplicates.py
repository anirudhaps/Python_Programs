'''
Exercise 10-9
'''

# from has_duplicates import has_duplicates

def remove_duplicates(lst):
    retlist = []
    i=0
    while i<len(lst)-1:
        if lst[i] not in lst[i+1:]:
            retlist.append(lst[i])
        i+=1
    retlist.append(lst[i])
    return retlist

n = int(raw_input('n = '))
l = []
print 'Enter '+ `n` +' numbers:'
for i in range(n):
    v = int(raw_input())
    l.append(v)
print remove_duplicates(l)
