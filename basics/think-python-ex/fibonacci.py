'''
Memos: python
'''
import time

stored_vals = {0:0, 1:1}

def fibonacci_V1(n):
    if n in stored_vals:        
        return stored_vals[n]
    val = fibonacci_V1(n-1) + fibonacci_V1(n-2)    
    stored_vals[n] = val
    return val

def fibonacci_V2(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci_V2(n-1) + fibonacci_V2(n-2)

n = int(raw_input('Enter n: '))
st = time.time()
print fibonacci_V1(n)
et = time.time() - st
print 'Time for v1:', et

st = time.time()
print fibonacci_V2(n)
et = time.time() - st
print 'Time for v2:', et
