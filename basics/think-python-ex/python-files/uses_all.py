'''
Exercise 9-5
'''

def uses_all(word,letters):
    retval = True
    for l in letters:
        if l not in word:
            retval = False
            break
    return retval

let = raw_input('letters: ')
count = 0
fin = open('words.txt')
for line in fin:
    l = line.strip()
    if uses_all(l,let):
        count+=1

print count
