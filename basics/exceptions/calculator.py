class Calculator:

    def __init__(self):
        pass

    def calc(self, x, y):
        try:
            div = int(x) / int(y)
            print 'x / y: %d' % div
        except ZeroDivisionError:
            print 'Divide by Zero Error'
        except ValueError:
            print 'Value Error'

    def getNums(self):
        import sys
        try:
            x = sys.argv[1]
            y = sys.argv[2]
            return x, y
        except IndexError:
            if len(sys.argv) < 3:
                print 'Usage: python %s <num1> <num2>' % sys.argv[0]
                print 'Using default values: x = 6 y = 3'
                x, y = 6, 3
                return x, y


if __name__ == '__main__':
    cobj = Calculator()
    x, y = cobj.getNums()
    cobj.calc(x, y)