'''
Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

last2('hixxhi') -> 1
last2('xaxxaxaxx') -> 1
last2('axxxaaxx') -> 2
'''

def last2(dstr):
    l2 = dstr[-2:]
    n = 0
    i = 0
    while i<len(dstr):
        if dstr[i:i+2]==l2:
            n+=1
        i+=1
    return n-1
    
print last2('hixxhi')
print last2('xaxxaxaxx')
print last2('axxxaaxx')
print last2('aaaaa')
