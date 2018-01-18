'''
Given a string, return recursively a "cleaned" string where adjacent chars that
are the same have been reduced to a single char. So "yyzzza" yields "yza". 

stringClean("yyzzza") → "yza"
stringClean("abbbcdd") → "abcd"
stringClean("Hello") → "Helo"
'''

def stringClean(s):
    l = len(s)
    if l==1:
        return s
    else:
        r = stringClean(s[1:])
        if s[0]!=r[0]:
            return s[0] + r
        else:
            return r

st = raw_input('Enter the string: ')
print 'Output: ' + str(stringClean(st))
