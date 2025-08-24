# -*- coding: utf-8 -*-


def calc(x, y):
    try:
        return x / y
    except (ZeroDivisionError, TypeError) as e:
        print(e)


def read_inp():
    x = int(input('num1: '))
    y = int(input('num2: '))
    return x, y


n1, n2 = read_inp()
ret = calc(n1, n2)
if ret is not None:
    print("num1 / num2: %d" % ret)