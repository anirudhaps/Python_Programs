
class classname:
	name = 'apsingh'
	age = 24
	def setname(self,n):
		self.name = n
	def setage(self,a):
		self.age = a
	def displayname(self):
		return self.name
	def displayage(self):
		return self.age

obj = classname()
print obj.displayname()
print obj.displayage()
obj.setname('Anirudha')
obj.setage(25)
print obj.name
print obj.age

#self is an alias for current object
#We must always refer an attribute of class as self.attributename inside a method
#otherwise simple attributename will give an error
