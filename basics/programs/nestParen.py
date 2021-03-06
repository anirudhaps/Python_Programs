﻿'''
Given a string, return true if it is a nesting of zero or more pairs of
parenthesis, like "(())" or "((()))". Suggestion: check the first and last
chars, and then recur on what's inside them. 

nestParen("(())") → true
nestParen("((()))") → true
nestParen("(((x))") → false
'''

def nestParen(s):
    l = len(s)
    if l<=1:
        return False
    elif l==2:
        if s[0]!='(':
            return False
        else:
            if s[1]!=')':
                return False
            else:
                return True
    else:
        if s[0]=='(' and s[l-1]==')':
            return nestParen(s[1:l-1])
        else:
            return False

st = raw_input('Enter the string: ')
print 'Output: ' + str(nestParen(st))
