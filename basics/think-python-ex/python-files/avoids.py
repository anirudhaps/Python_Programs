'''
Exercise 9-3
'''

def avoids(word,forbid):
    retval = True
    for l in forbid:
        if l in word:
            retval = False
            break
    return retval

#w = raw_input('Word: ')
f = raw_input('Forbidden string: ')
count = 0
fin = open('words.txt')
for line in fin:
    l = line.strip()
    if avoids(l,f):
        count+=1

print 'No of words that avoid ' + f + ' are:', count
#print w, 'avoids', f, ':', avoids(w,f)    
