'''
Given a string, compute recursively (no loops) the number of "11" substrings in
the string. The "11" substrings should not overlap. 

count11("11abc11") → 2
count11("abc11x11x11") → 3
count11("111") → 1
'''

def count11(s):
    l = len(s)
    if l<2:
        return 0
    elif l==2:
        if s=='11':
            return 1
        else:
            return 0
    else:
        if s[0:2]=='11':
            return 1 + count11(s[2:])
        elif s[0]!='1' and s[1]=='1':
            return count11(s[1:])
        else:
            return count11(s[2:])

st = raw_input('Enter the string: ')
print 'Output: ' + str(count11(st))
