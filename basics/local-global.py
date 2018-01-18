# study of local and global variables and globals() and locals() functions
x = 10
y = 20

def func():
    # print sum([x,y]) # error because local variable x is referenced before
    # assignment. Since, x is used inside func() as a local variable, x in
    # above statement will not be treated as a global variable.
    x = 32
    y = 12
    print sum([x,y])
    print 'global dict: ', globals(), '\n'
    print 'local dict: ', locals(), '\n'
    s = x + globals()['y']
    print s

func()
