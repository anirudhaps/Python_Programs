# study of class and instance variables

class A:
    m = 0 # this is a class member and is accessed by all the instances of this
          # class A
    k = 3      
    def init(self):
        A.m+=1
        self.m = 0 #this is an instance variable and is specific to an instance 

    def disp(self):
        m = 5 # this is a local variable of this function
        print 'Value of class variable m = ' + `A.m`
        print 'Value of instance variable m = ' + `self.m`
        print 'local m = ' + `m` 


ob1 = A()
ob1.init()
ob1.disp()
print '-------------'
ob2 = A()
ob2.init()
ob2.disp()
print '-------------'
print ob1.m  # = 0
print ob2.m  # = 0
print A.m  # = 2
print '-------------'
print ob1.k  # = 3
print ob2.k  # = 3
print A.k  # = 3
