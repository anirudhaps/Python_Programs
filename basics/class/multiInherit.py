# multiple inheritance of classes

class Father:
    name1 = "I am dad"

class Mother:
    name2 = "I am mom"

class child(Father,Mother):
    pass

# pass means do nothing

cob = child()
print cob.name1
print cob.name2
