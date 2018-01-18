'''
Given a string and a non-empty substring sub, compute recursively the number
of times that sub appears in the string, without the sub strings overlapping. 

strCount("catcowcat", "cat") → 2
strCount("catcowcat", "cow") → 1
strCount("catcowcat", "dog") → 0
'''

def strCount(s,sub):
    ls = len(s)
    lsub = len(sub)
    if ls<lsub:
        return 0
    elif ls==lsub:
        if s==sub:
            return 1
        else:
            return 0
    else:
        if s[0:lsub]==sub:
            return 1 + strCount(s[lsub:],sub)
        else:
            return strCount(s[1:],sub)

st = raw_input('Enter a string: ')
subst = raw_input('Enter the substring: ')
print 'No. of substrings %s in string %s = %d' % (subst,st,strCount(st,subst))
