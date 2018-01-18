'''
Exercise 9-2
'''

def has_no_e(word):
    if 'e' not in word:
        return True
    else:
        return False
        
fin = open('words.txt')
total = 0
count = 0
for line in fin:
    total+=1    
    l = line.strip()
    if has_no_e(l):
        count+=1
        print l

per = count * 100.0 / total
print 'No of words with no \'e\':', count 
print 'Percentage of words with no \'e\':', per
