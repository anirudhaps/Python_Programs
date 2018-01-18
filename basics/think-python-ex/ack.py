'''
Ackermann function, A(m,n): Exercise 6.5
'''

def ack(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1,ack(m,n-1))
    else:
        print 'invalid input'

a = int(raw_input('m = '))
b = int(raw_input('n = '))
print ack(a,b)
