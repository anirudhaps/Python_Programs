#comparison operators
#>,>=,<,<=,==,!=,in,is

studentnames = raw_input('Enter a sequence of student names:')
print 'studentnames:', studentnames
if 'anirudha' in studentnames:
    print 'anirudha is available'
else:
    print 'anirudha is not available'

if 'virat' in studentnames:
    print 'virat is available'
else:
    print 'virat is not available'

lone = [1,2,3,4]
ltwo = [1,2,3,4]

if lone is ltwo:
    print 'lone is ltwo'
else:
    print 'lone is not ltwo'

lt = lf = [4,5,6,7]

if lt is lf:
    print 'lt is lf'
else:
    print 'lt is not lf'

if lone==ltwo:
    print 'content of lone and ltwo is same'
else:
    print 'content of lone and ltwo is not same'


lst = [23,43,25,34,65]
print lst
if 23 in lst:
    print '23 is in lst'
else:
    print '23 is not in lst'

if 39 in lst:
    print '39 is in lst'
else:
    print '39 is not in lst'



    
