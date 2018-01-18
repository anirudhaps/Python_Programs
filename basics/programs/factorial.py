# factorial using recursion

def fact(n):
	if n==0 or n==1:
		return 1
	else:
		return (n * fact(n-1))

k = input('Enter any number>=0: ')
print 'The factoral of %d is %d' % (k,fact(k))