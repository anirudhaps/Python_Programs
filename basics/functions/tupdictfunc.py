#passing predefined tuple or dictionary as parameter to a function

def prtuple(a,b,c):
    print(a*b+c)

#def prtuple(*k):    
    #print(k)

def prdict(**dic):
    print(dic)

t = (2,5,7)
prtuple(*t)   # when a tuple is passed to a function as parameter, use * before
              # the name of the tuple
#w = (2,3,4,5,6) 
#prtuple(*w) #error! prtuple can take only 3 arguments but w is providing 5 args

d = {'dad':43, 'mom':34, 'sis':10}
prdict(**d)  #use ** before dictionary name while passing it as parameter
