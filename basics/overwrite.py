#overwriting variables during inheritance

class parent:
    name = "apsingh"
    age = 23

class child(parent):
    age = 24
    sex = "male"

pob = parent()
cob = child()
print "printing parent's credentials:"
print pob.name
print pob.age
print "printing child's credentials:"
print cob.name
print cob.age
print cob.sex


    
