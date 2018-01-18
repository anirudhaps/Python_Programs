# passing a number by value to a function

def inc(x):
    x = x+1
    return x

n = 10
print 'Before calling inc(x), n = ' + `n`
n = inc(n)
print 'After calling inc(x), n = ' + `n`


# passing a number by reference

def incre(x):
    'x here is a list having only one element'
    x[0] = x[0] + 1


n = [20]
print 'Before calling incre(x), n = ' + `n`
incre(n)
print 'After calling incre(x), n = ' + `n`
