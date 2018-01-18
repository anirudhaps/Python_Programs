'''
Given two int values, return their sum. Unless the two values are the same, then return double their sum.

sum_double(1, 2) -> 3
sum_double(3, 2) -> 5
sum_double(2, 2) -> 8
'''
import sys

def sumDob(a,b):
    s = a + b
    if a==b:
        return 2 * s
    else:
        return s
        

print sumDob(int(sys.argv[1]),int(sys.argv[2]))
# Imp: if we don't typecast to int for both command-line arguments, they are taken as strings 
# and thus, s = concatenation of a and b
