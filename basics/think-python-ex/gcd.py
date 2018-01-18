'''
compute gcd using euclidean algorithm
'''

def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    elif a==1 or b==1:
        return 1
    else:
        r = a%b
        return gcd(a,r)

a = int(raw_input('a='))
b = int(raw_input('b='))
print gcd(a,b)
