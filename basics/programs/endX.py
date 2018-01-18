'''
Given a string, compute recursively a new string where all the lowercase 'x'
chars have been moved to the end of the string. 

endX("xxre") → "rexx"
endX("xxhixx") → "hixxxx"
endX("xhixhix") → "hihixxx"
'''

def endX(s):
    l = len(s)
    if l==1:
        return s
    else:
        if s[0]=='x':
            return endX(s[1:]) + s[0]
        else:
            return s[0] + endX(s[1:])

st = raw_input('Enter any string: ')
print 'endX output: ' + endX(st)
