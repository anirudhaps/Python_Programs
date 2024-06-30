name = input("What is your name? ")
print(f"Hello, {name}!")

age = input("How old are you? ")
if type(age) is str:
    print("Converting it to int...")
    age = int(age)
print(f"your age is {age}")

pi = input("What is the value of PI? ")
pi = float(pi)
area = pi * 3 * 3
print(f"Area of circle is {area}")