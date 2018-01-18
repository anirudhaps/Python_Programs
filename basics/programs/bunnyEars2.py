# We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the normal 2 ears. 
# The even bunnies (2, 4, ..) we'll say have 3 ears, because they each have a raised foot. 
# Recursively return the number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication). 

# bunnyEars2(0) -- 0
# bunnyEars2(1) -- 2
# bunnyEars2(2) -- 5

def bunnyEars(n):
	if n==0:
		return 0
	else:
		r = bunnyEars(n-1)
		k = n%2
		if k==0:
			return r+3
		else:
			return r+2


no = input('Enter the number of bunnies: ')
print 'The total number of ears of %d bunnies is %d' % (no,bunnyEars(no))