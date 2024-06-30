roll_no = [1, 2, 3, 4]
print(roll_no)
for num in roll_no:
    print(num)

# append new roll number
roll_no.append(5)
print(roll_no)
first_roll_no = roll_no[0]
last_roll_no = roll_no[-1]
print(f"first and last roll numbers are: {first_roll_no}, {last_roll_no} respectively.")

first_three = roll_no[:3]
print(first_three)

copied = roll_no[:]
print(copied)
# update a value in the list
copied[2] = 9
print(copied)

if 3 in roll_no:
    print("3 is present in the list")

if 7 not in roll_no:
    print("7 not in the list")

squares = []
for num in range(1, 11):
    squares.append(num ** 2)

print(squares)

cubes = [num ** 3 for num in range(1, 11)]
print(cubes)
