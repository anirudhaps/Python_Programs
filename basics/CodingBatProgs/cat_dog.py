'''
Return True if the string "cat" and "dog" appear the same number of times in the given string.

cat_dog('catdog') -> True
cat_dog('catcat') -> False
cat_dog('1cat1cadodog') -> True
'''

import sys

def cat_dog(dstr):
    cats = 0
    dogs = 0
    i = 0
    while i<len(dstr)-2:
        if dstr[i:i+3]=='cat':
            cats+=1
        elif dstr[i:i+3]=='dog':
            dogs+=1
        i+=1
    return cats==dogs

print cat_dog(sys.argv[1])
