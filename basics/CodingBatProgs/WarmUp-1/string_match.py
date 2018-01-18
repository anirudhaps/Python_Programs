'''
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

string_match('xxcaazz', 'xxbaaz') -> 3
string_match('abc', 'abc') -> 2
string_match('abc', 'axc') -> 0
'''

def string_match(a,b):
    if len(a)<len(b):
        s = len(a)
    else:
        s = len(b)
    i=0
    n=0
    while i<s-1:
        astr = a[i:i+2]
        bstr = b[i:i+2]
        if astr==bstr:
            n+=1
        i+=1
    return n

print string_match('xxcaazz','xxbaaz')
print string_match('abc','abc')
print string_match('abc','axc')
