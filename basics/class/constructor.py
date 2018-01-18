# constructors

class myclass:
    name = "apsingh"
    def __init__(self,s):
        self.name = s
    def prname(self):
        print self.name
	print myclass.name


# __init__() is the constructor

obj = myclass("Amit")
obj.prname()
