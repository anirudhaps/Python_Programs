'''
Given a string that contains a single pair of parenthesis, compute recursively
a new string made of only of the parenthesis and their contents, so
"xyz(abc)123" yields "(abc)". 

parenBit("xyz(abc)123") → "(abc)"
parenBit("x(hello)") → "(hello)"
parenBit("(xy)1") → "(xy)"
'''
import string

def parenBit(s):
    l = len(s)
    if l==1:
        return ''
    else:
        k1 = string.find(s,'(')
        k2 = string.find(s,')')
        if k1!=-1 and k2!=-1:
            if k1>k2:
                return ''
            else:
                if s[0]!='(':
                    return parenBit(s[1:])
                else:
                    return s[0:k2+1]
        else:
            return ''

st = raw_input('Enter the string: ')
print 'Output: ' + parenBit(st)
