'''
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') -> 'CCoCodCode'
string_splosion('abc') -> 'aababc'
string_splosion('ab') -> 'aab'
'''
import sys

def string_splosion(dstr):
    l = len(dstr)
    i = 1
    out = ''
    while i<=l:
        out = out + dstr[0:i]
        i+=1
    return out

print string_splosion(sys.argv[1])
