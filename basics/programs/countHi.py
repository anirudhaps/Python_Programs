'''
Given a string, compute recursively (no loops) the number of times lowercase
"hi" appears in the string. 

countHi("xxhixx") → 1
countHi("xhixhix") → 2
countHi("hi") → 1
'''

def countHi(s):
    l = len(s)
    if l==0 or l==1:
        return 0
    elif l==2:
        if s[0]=='h' and s[1]=='i':
            return 1
        else:
            return 0
    else:        
        if s[0]=='h' and s[1]=='i':
            return 1 + countHi(s[2:])
        else:
            return countHi(s[1:])


st = raw_input('Enter the string: ')
print 'The number of hi in string %s is %d' % (st,countHi(st))
