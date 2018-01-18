# passing a dictionary to a function

# method-1

def dictfunc(**d):
    print 'For method-1:'
    print d


d1 = {'a':5, 'b':10, 'c':20}
dictfunc(**d1)

# method-2

def dictfunc2(d):
    print 'For method-2:'
    print d

dictfunc2(d1)


# method-3

def dictfunc3(*d):
    print 'For method-3:'
    print d

dictfunc3(d1)
# here d1 will be passed as a dictionary, but inside dictfunc3() it will become
# part of the tuple d
