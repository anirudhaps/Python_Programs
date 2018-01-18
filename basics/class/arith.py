# class to test same name local variables in a class

class arith:
    x = 0
    def incre(self,x):
        self.x = self.x + x

    def display(self):
        print 'Value of x = ' + `self.x`


ob = arith()
ob.display()
ob.incre(5)
print 'After increment:'
ob.display()
