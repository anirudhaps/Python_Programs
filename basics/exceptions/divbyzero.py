def divide():
    try:
        x = input('Enter num1: ')
        y = input('Enter num2: ')
        div = x / y
        print 'x / y = %d' % div
    except ZeroDivisionError:
        print 'x, y = %d, %d' % (x, y)
        print 'Divide by zero error'


if __name__ == '__main__':
    divide()