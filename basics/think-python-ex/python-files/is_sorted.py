'''
Exercise 10-7
'''

#def is_sorted(l):
    #i=0
    #while i<len(l)-1:
        #if l[i]>l[i+1]:
            #return False
        #i+=1
    #return True

def is_sorted(l):
    cur = l[0]
    for i in l:
        if i<cur:
            return False
        cur = i
    return True


lst = [1,3,3]
print is_sorted(lst)
