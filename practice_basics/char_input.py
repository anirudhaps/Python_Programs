"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will
turn 100 years old.
"""


def read_input():
    name = input('Please enter your name: ')
    try:
        age = int(input('Enter your age: '))
    except ValueError:
        print("error: invalid number")
    return name, age


def print_hund_age_year(name, age):
    import datetime
    # get current date and time
    now = datetime.datetime.now()
    hundred_age_year = now.year + (100 - age)
    print(f'Hi {name}, you will turn 100 years old in year {hundred_age_year}')


if __name__ == '__main__':
    name, age = read_input()
    print_hund_age_year(name, age)