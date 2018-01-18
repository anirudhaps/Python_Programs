'''
We'll say that a "pair" in a string is two instances of a char separated by a
char. So "AxA" the A's make a pair. Pair's can overlap, so "AxAxA" contains 3
pairs -- 2 for A and 1 for x. Recursively compute the number of pairs in the
given string. 

countPairs("axa") → 1
countPairs("axax") → 2
countPairs("axbx") → 1
'''

def countPairs(s):
    l = len(s)
    if l<=2:
        return 0
    else:
        if s[0]==s[2]:
            return 1 + countPairs(s[1:])
        else:
            return countPairs(s[1:])

st = raw_input('Enter the string: ')
print 'No of pairs in string %s are: %d' % (st,countPairs(st))
