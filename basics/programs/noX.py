'''
Given a string, compute recursively a new string where all the 'x' chars have
been removed. 

noX("xaxb") → "ab"
noX("abc") → "abc"
noX("xx") → ""
'''

def noX(s):
    l = len(s)
    if l==0:
        return ''
    elif l==1:
        if s=='x':
            return ''
        else:
            return s
    else:
        if s[0]=='x':
            return noX(s[1:])
        else:
            return s[0] + noX(s[1:])
    
st = raw_input('Enter the string: ')
print 'After removing all x: ' + noX(st)
    
