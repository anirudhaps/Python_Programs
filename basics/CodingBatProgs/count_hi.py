'''
Return the number of times that the string "hi" appears anywhere in the given string.

count_hi('abc hi ho') -> 1
count_hi('ABChi hi') -> 2
count_hi('hihi') -> 2
'''
import sys

def count_hi(dstr):
    count = 0
    if 'hi' in dstr:
        i = 0        
        while i<len(dstr)-1:
            if dstr[i:i+2]=='hi':
                count+=1
                i+=1
            i+=1     
    return count    


print count_hi(sys.argv[1])
