# -*- coding: utf-8 -*-


def calc(x, y):
    try:
        ret = x / y
    except Exception, e:
        print 'Invalid Input:', e
    else:
        print 'Operation successful'
        return ret
    finally:
        print 'Cleaning up'


if __name__ == '__main__':
    x = input('Enter num1: ')
    y = input('Enter num2: ')
    ret = calc(x, y)
    if ret is not None:
        print 'num1 / num2:', ret
