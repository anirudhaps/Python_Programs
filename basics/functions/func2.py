#multiply by hundred

def mulhund(x):
    return x*100

num = int(input('Enter any number: '))
hn = mulhund(num)
##print 'Hundred times it is ' + `hn`
k = (num, hn)
print('Hundred times %d is %d' % k)


