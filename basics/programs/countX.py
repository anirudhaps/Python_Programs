'''
Given a string, compute recursively (no loops) the number of lowercase 'x'
chars in the string. 

countX("xxhixx") → 4
countX("xhixhix") → 3
countX("hi") → 0
'''

def countX(s):
    if s=='':
        return 0
    else:
        if s[0]=='x':
            return 1 + countX(s[1:])
        else:
            return countX(s[1:])

inp = raw_input('Enter the string: ')
print 'No. of lowercase x in %s is %d' % (inp,countX(inp))
