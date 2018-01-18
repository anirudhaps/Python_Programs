'''
Given a string, compute recursively (no loops) a new string where all
appearances of "pi" have been replaced by "3.14". 

changePi("xpix") → "x3.14x"
changePi("pipi") → "3.143.14"
changePi("pip") → "3.14p"
'''

def changePi(s):
    l = len(s)
    lst = list(s)
    if l==0 or l==1:
        return s
    elif l==2:
        if s[0]=='p' and s[1]=='i':
            lst[0:] = ['3','.','1','4']
            
            
            
