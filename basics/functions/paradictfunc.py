#passing parameters to a function to print them in the form of a dictionary

def familyAges(**ages):   #**ages will print everything passed in the form of 
    print('Family ages:')  # a dictionary
    print(ages)

def combined(name,*point,**famages):
    s=0
    for p in point:
        s+=p
    avg=float(s)/len(point)
    print(name + ' has following points in exams and family ages:')
    print(point, avg)
    print(famages)


familyAges(dad=52,mom=49,bro=24,sis=15) #but you have to pass the parameters
#like as it is done above

combined('Devesh',7,8,9,9,8,9,mom=49,dad=52,sis=16)

# two ways of combining a number with string and printing it:
val = 5
print('hello ' + str(val))        # method-1
print('hello %s' % (val))         # method-3

