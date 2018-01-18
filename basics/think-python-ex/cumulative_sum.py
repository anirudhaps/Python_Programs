'''
Exercise 10-3
'''

def cumulative_sum(l):
    ret = []
    s = 0
    for i in l:
        s+=i
        ret.append(s)
    return ret


lst = []
for i in range(5):
    lst.append(int(raw_input('Enter a number: ')))

print 'Original list:', lst
print 'Cumulative sum:', cumulative_sum(lst)
