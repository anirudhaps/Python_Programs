'''
Exercise 7.3
'''
import math

def estimate_pi():
    a = 2*math.sqrt(2)/9801
    b = 1e-15
    s = 0.0
    k = 0
    while True:
        term = (math.factorial(4*k)*(1103 + 26390*k))/(math.factorial(k)**4 * 396**(4*k))        
        if term<b:
            break
        s+=term
        k+=1
    c = a * s
    return 1/c
    
val = estimate_pi()
print 'Computed value of pi:', val
print 'Actual value of pi:', math.pi

