'''
Given a string, compute recursively a new string where identical chars that
are adjacent in the original string are separated from each other by a "*". 

pairStar("hello") → "hel*lo"
pairStar("xxyy") → "x*xy*y"
pairStar("aaaa") → "a*a*a*a"
'''

def pairStar(s):
    l = len(s)
    if l==1:
        return s
    else:
        if s[1]==s[0]:
            return s[0] + '*' + pairStar(s[1:])
        else:
            return s[0] + pairStar(s[1:])

st = raw_input('Enter any string: ')
print 'pairStar output: ' + pairStar(st)
            
