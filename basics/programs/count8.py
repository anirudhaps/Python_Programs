'''
Given a non-negative int n, compute recursively (no loops) the count of the
occurrences of 8 as a digit, except that an 8 with another 8 immediately to
its left counts double, so 8818 yields 4. Note that mod (%) by 10 yields the
rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost
digit (126 / 10 is 12). 

count8(8) → 1
count8(818) → 2
count8(8818) → 4
'''

def count8(n):
    if n==0:
        return 0
    else:
        k1 = n%10
        n = n/10
        k2 = n%10
        if k1==8 and k2==8:
            return 2 + count8(n)
        elif k1==8:
            return 1 + count8(n)
        else:
            return count8(n)


no = input('Enter any number: ')
print 'Output of count8(%d) is %d' % (no,count8(no))
