# passing a tuple to a function

# method-1
def tupfunc(*tup):
    print 'For method-1:'
    print tup


t = (1,2,3)
tupfunc(*t)
tupfunc(2, 3, 4)


# method-2

def tupfunc2(tup):
    print 'For method-2:'
    print tup


tupfunc(t)
tupfunc2(t)
# the difference between the above methods is cleared by seeing the output
# of the program
