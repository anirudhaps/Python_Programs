'''
Given a non-negative int n, return the sum of its digits recursively
(no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
while divide (/) by 10 removes the rightmost digit (126 / 10 is 12). 

sumDigits(126) → 9
sumDigits(49) → 13
sumDigits(12) → 3
'''

def sumDigits(n):
    r = n % 10
    if r==n:
        return r
    else:
        return r + sumDigits(n/10)


k = input('Enter the number: ')
print 'Sum of the digits of number %d is %d' % (k, sumDigits(k))
