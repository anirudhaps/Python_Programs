'''
Given a string, compute recursively a new string where all the adjacent chars
are now separated by a "*". 

allStar("hello") → "h*e*l*l*o"
allStar("abc") → "a*b*c"
allStar("ab") → "a*b"
'''

def allstar(s):
    l = len(s)
    if l==1:
        return s
    else:
        return s[0] + '*' + allstar(s[1:])


st = raw_input('Enter any string: ')
print '********AllStars*************'
print allstar(st)
