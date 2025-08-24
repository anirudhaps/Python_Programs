# string studies

name = 'apsingh'

print(name)  # prints apsingh
print(name[0]) # prints a
print(name[1]) # prints p

print(f'I am {name} and my age is {24}')
# above line will print: I am apsingh and my age is 24

print(name.upper()) # prints the name, apsingh in uppercase: APSINGH
age = 24
print('I am ' + name + ' and my age is ' + str(age))
# above line will print: I am apsingh and my age is 24
#or
print(f'I am {name} and my age is {age}')
# print('I am ' + name + ' and my age is ' + age)  # error: can't concatenate
# a string to an int
