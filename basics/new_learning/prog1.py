def read_input():
    num = input('Enter any number: ')
    return num


def check_even():
    num = read_input()
    if num % 2 == 0:
        print 'Even number'
    else:
        print 'Odd number'


def check_dig_type():
    num = read_input()
    if num >= 0 and num <= 9:
        print 'Single digit number'
    elif num >= 10 and num <= 99:
        print 'Two digit number'
    else:
        print '3 or more number digits in the number'


if __name__ == '__main__':
    check_even()
    check_dig_type()