#and-or study

num = int(input('Enter any whole number:'))

if num>=0 and num<=9:
    print('It is a single digit number')
elif num>=10 and num<=99:
    print('It is a double digit number')
else:
    if num<0:
        print('It is a negetive number')
    else:
        print('It has three or more digits')
     
t = num%2
th = num%3

if t==0 or th==0:
    print('The number is divisible by either 2 or 3 or both')
else:
    print('The number is neither divisible by 2 nor by 3')
