# -*- coding: utf-8 -*-
# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies recursively
# (without loops or multiplication). 

# bunnyEars(0) → 0
# bunnyEars(1) → 2
# bunnyEars(2) → 4

def bunnyEars(n):
    if n==0:
        return 0
    # elif n==1:
        # return 2
    else:
        return 2 + bunnyEars(n-1)


k = input('Enter the number of bunnies: ')
print 'The total number of ears of %d bunnies is %d' % (k,bunnyEars(k))
