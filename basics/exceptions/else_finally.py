# -*- coding: utf-8 -*-

def calc(x, y):
    try:
        ret = x / y
        # return ret
    except Exception as e:
        print(e)
    else:
        print('Operation successful')
        return ret
    finally:
        print('Cleaning up')


if __name__ == '__main__':
    x = int(input('Enter num1: '))
    y = int(input('Enter num2: '))
    ret = calc(x, y)
    if ret is not None:
        print(f'num1 / num2: {round(ret, 3)}')
