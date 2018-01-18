# fibonacci series
# 0 1 1 2 3 5 8 13 21 ...
# find nth fibonacci number

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
        


k = input('Enter the value of n: ')
print 'The fibonacci number for n = ' + `k` + ' is:'
print fibo(k)

