'''
Given a string, compute recursively the number of times lowercase "hi" appears
in the string, however do not count "hi" that have an 'x' immedately before them. 

countHi2("ahixhi") → 1
countHi2("ahibhi") → 2
countHi2("xhixhi") → 0
'''

def countHi2(s):
    l = len(s)
    if l<2:
        return 0
    elif l==2:
        if s=='hi':
            return 1
        else:
            return 0
    elif l==3:
        if s[0]!='x':
            if s[1]=='h' and s[2]=='i':
                return 1
            else:
                return 0
        else:
            return 0
    else:
        if s[0]!='x':
            if s[1]=='h' and s[2]=='i':
                return 1 + countHi2(s[3:])
            else:
                return countHi2(s[3:])
        else:
            return countHi2(s[3:])


st = raw_input('Enter the string: ')
print 'Output: ' + str(countHi2(st))
