'''
A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function
called is_power that takes parameters a and b and returns True if a is a power of b . Note:
you will have to think about the base case.
'''
from sys import argv

def is_power(a,b):    
    if b==0 and a!=0:
        return False
    elif b==0 and a==0:
        return True
    elif b==1 and a!=1:
        return False
    elif b==1 and a==1:
        return True
    elif a==0:
        return False
    #else:
        #if a<1:
            #return False
    if a%b==0:        
        frac = a/b
        if frac==1:
            return True
        else:        
            return is_power(frac,b)        
    else:
        return False
        
a = int(argv[1])
b = int(argv[2])
print is_power(a,b)
