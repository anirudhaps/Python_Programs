#iterative program to generate fibonacci series

fibo = [0,1]
num = input('Enter the number of fibonacci numbers to be printed: ')
for i in range(num-2):
    fibo.append(fibo[-2] + fibo[-1])

print fibo
