# string studies

name = 'apsingh'

print name  # prints apsingh
print name[0] # prints a
print name[1] # prints p

print 'I am %s and my age is %d' % (name, 24)
# above line will print: I am apsingh and my age is 24

print name.upper() # prints the name, apsingh in uppercase: APSINGH
age = 24
print 'I am ' + name + ' and my age is ' + `age`
# above line will print: I am apsingh and my age is 24
#or
print 'I am ' + name + ' and my age is ' + str(age)
print 'I am ' + name + ' and my age is ' + age  # error: can't concatenate
# a string to an int
