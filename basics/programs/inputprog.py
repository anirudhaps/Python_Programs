# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.

name = raw_input('Enter your name: ')
age = input('Enter your age: ')
diff = 100 - age
hage = 2015 + diff
pr = name + ', In year ' + `hage` + ', you will be 100 years old.'
no = input('Enter the number of times you want to print the message: ')
i=0
while i<no:
	print pr
	i = i+1
# print '%s, In year %d, you will be 100 years old.' % (name,hage)