#inheritance

class parentClass:
    x=0
    y=0
    def setCoord(self,a,b):
        self.x=a
        self.y=b
    def printCoord(self):
        print '(%d,%d)' % (self.x,self.y)

class childClass(parentClass):    
    def setoff(self,ox,oy):
        self.x = self.x + ox
        self.y = self.y + oy


cob = childClass()
cob.setCoord(2,5)
cob.printCoord()
cob.setoff(3,3)
cob.printCoord()

