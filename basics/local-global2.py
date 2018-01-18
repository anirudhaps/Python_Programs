# reassigning a global variable in side a function

x = 5
def func():
    # x = 10 will not work because it will create a new local variable with same
    # name x
    global x
    x = 10

print 'global x before reassignment: ' + `x`
func()
print 'global x after reassignment: ' + `x`
