#handling variable number of paramaters to a function

def visited(name,*places):
    print name + ' has visited the following places:'
    print places  #here places is a tuple containing multiple item
    print 'same places:'
    for p in places:
        print p


visited('Anirudha','Ahmedabad','Etawa','Delhi','Hyderabad','Jodhpur')
#visited(23,23,4,5,6,7,89)
