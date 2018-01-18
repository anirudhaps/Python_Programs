# super class and sub-class study

class Filter:
    def init(self):
        self.blocked = []

    def filterIt(self,seq):
        return filter(lambda x: x not in self.blocked, seq)

class SpamFilter(Filter):
    def init(self):
        self.blocked = ['spam']


f = Filter()
f.init()
print f.filterIt(['hello','world'])

sf = SpamFilter()
sf.init()
print sf.filterIt(['spam','hello','spam','Thorin','spam','spam','Thrain'])
