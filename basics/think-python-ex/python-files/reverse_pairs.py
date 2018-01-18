'''
Exercise 1-12
'''

def reverse_pairs(lst):    
    l = lst[:]    
    for w in l:
        #print 'entered'
        i=l.index(w)+1
        while i<len(l):
            r = list(l[i])
            r.reverse()
            r = ''.join(r)
            if w==r:
                print w, '<-->', l[i]                
                #l.remove(w)
                #l.remove(l[i])
                break
            i+=1        

lst = ['aps','rps','dps','spa','spd','spk','kjh']
print lst
print 'Reverse pairs are:'
reverse_pairs(lst)
