'''
Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb') -> 1
count_code('codexxcode') -> 2
count_code('cozexxcope') -> 2
'''

from sys import argv

def count_code(dstr):
    count = 0
    i=0
    while i<len(dstr)-3:
        s = dstr[i:i+4]
        if s[0:2]=='co' and s[-1]=='e':
            count+=1
        i+=1
    return count


print count_code(argv[1])
