#creating a class and an object

class firstClass:
    name = "Anirudha Pratap Singh"
    age = 23

    def getAge(self):
        return self.age

    def getname(self):
        return self.name


obj = firstClass()
print obj.age
print obj.name
print obj.getname()
print obj.getAge()
