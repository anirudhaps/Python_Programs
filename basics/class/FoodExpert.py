# a class

class FoodExpert:
    def init(self):
        self.goodfood = []

    def addGoodFood(self,item):
        self.goodfood.append(item)

    def getGoodFood(self):
        return self.goodfood

    def likes(self,x):
        return x in self.goodfood

    def prefers(self,x,y):
        xi = self.goodfood.index(x)
        yi = self.goodfood.index(y)
        if xi<yi:
            return x
        else:
            return y


f = FoodExpert()
f.init()
map(f.addGoodFood,['soyabean','palak','paneer','chole','vada'])
print f.goodfood
print filter(f.likes,['chicken','mutton','egg','vada','soyabean','chapatti'])
print reduce(f.prefers,f.goodfood)
'''f.addGoodFood('soyabean')
f.addGoodFood('palak')
f.addGoodFood('paneer')
print f.goodfood
print f.getGoodFood()
print f.likes('burger')
print f.likes('palak')
print f.prefers('palak','paneer')'''


