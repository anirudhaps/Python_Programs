"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will
turn 100 years old.
"""


def read_input():
    name = raw_input('Please enter your name: ')
    age = input('Enter your age: ')
    msg_disp_count = input('Enter message display count: ')
    return name, age, msg_disp_count


def print_hund_age_year(name, age, msg_disp_count):
    import datetime
    # get current date and time
    now = datetime.datetime.now()
    hundred_age_year = now.year + (100 - age)
    msg = 'Hi %s, you will turn 100 years old in year %s' \
    % (name, hundred_age_year)
    print (msg + ' ') * msg_disp_count
    print (msg + '\n') * msg_disp_count


if __name__ == '__main__':
    name, age, msg_count = read_input()
    print_hund_age_year(name, age, msg_count)