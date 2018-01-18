'''
check for palindrome
'''

from sys import argv

def is_palindrome(dstr):
    if len(dstr)<=1:
        return True
    if dstr[0]!=dstr[-1]:
        return False
    else:
        return is_palindrome(dstr[1:-1])

print is_palindrome(argv[1])
