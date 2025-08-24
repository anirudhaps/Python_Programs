class Dog:
    pass

dog1 = Dog()
dog2 = Dog()

print(type(dog1))
print(isinstance(dog1, Dog))
print(isinstance(dog2, Dog))
print(dog1 is dog2)
print(dog1 is not dog2)

x = 5
print(isinstance(x, int))
print(isinstance(x, Dog))