'''
Count recursively the total number of "abc" and "aba" substrings that appear
in the given string. 

countAbc("abc") → 1
countAbc("abcxxabc") → 2
countAbc("abaxxaba") → 2
'''

def countAbc(s):
    l = len(s)
    if l<3:
        return 0
    elif l==3:
        if s=='abc' or s=='aba':
            return 1
        else:
            return 0
    else:
        if s[0:3]=='abc' or s[0:3]=='aba':
            return 1 + countAbc(s[3:])
        else:
            return countAbc(s[1:])

st = raw_input('Enter the string: ')
print 'Output: ' + str(countAbc(st))
