def divide():
    try:
        x = int(input('Enter num1: '))
        y = int(input('Enter num2: '))
        div = x / y
        print(f'x / y = {div}')
    except ZeroDivisionError as e:
        print(e)


if __name__ == '__main__':
    divide()