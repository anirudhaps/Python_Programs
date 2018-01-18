'''
Exercise 10-7
'''

def is_anagram(a,b):
    lb = list(b)
    if len(a)!=len(b):
        return False
    i=0
    while i<len(a):
        if a[i] in lb:
            lb.remove(a[i])
        else:
            return False
        i+=1
    if len(lb)==0:
        return True

s1 = raw_input('Word-1: ')
s2 = raw_input('Word-2: ')
print 'is_anagram('+s1+','+s2+')?',is_anagram(s1,s2)
