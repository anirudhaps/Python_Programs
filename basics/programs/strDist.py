'''
Given a string and a non-empty substring sub, compute recursively the largest
substring which starts and ends with sub and return its length. 

strDist("catcowcat", "cat") → 9
strDist("catcowcat", "cow") → 3
strDist("cccatcowcatxx", "cat") → 9
'''

def strDist(s,sub):
    ls = len(s)
    lsub = len(sub)
    if lsub==0 or ls==0:
        return 0
    elif ls==lsub:
        if s==sub:
            return lsub
        else:
            return 0
    elif ls<lsub:
        return 0
    else:
        if ls>=(2*lsub):
            if s[0:lsub]==sub and s[ls-lsub+1:]==sub:
                return ls
            elif s[0:lsub]!=sub:
                if s[ls-lsub+1:]!=sub:
                    return strDist(s[lsub:ls-lsub+1],sub)
                else:
                    return strDist(s[1:],sub)
            else:
                return strDist(s[0:ls-1],sub)
        else:
            if s[0:lsub]==sub and s[ls-lsub+1:]==sub:
                return ls
            else:
                return 0


st = raw_input('Enter the string: ')
subst = raw_input('Enter the substring: ')
print 'Output: ' + str(strDist(st,subst))
