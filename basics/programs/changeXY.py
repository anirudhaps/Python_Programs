'''
Given a string, compute recursively (no loops) a new string where all the
lowercase 'x' chars have been changed to 'y' chars. 

changeXY("codex") → "codey"
changeXY("xxhixx") → "yyhiyy"
changeXY("xhixhix") → "yhiyhiy"
'''
import sys

def changeXY(s):
    l = len(s)
    if l==0:
        return ''
    else:
        if s[0]=='x':
            #print 'y',
            sys.stdout.write('y') #doesn't print space or newline after 'y'
        else:
            #print s[0],
            sys.stdout.write(s[0])
        if l>=2:
            changeXY(s[1:])

st = raw_input('Enter the string: ')
print 'The substituted string is: '
changeXY(st)
        
