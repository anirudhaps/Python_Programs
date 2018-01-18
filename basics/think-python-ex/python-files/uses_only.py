'''
Exercise 9-4
'''

def uses_only(word,letters):
    retval = True
    for l in word:
        if l not in letters:
            retval = False
            break
    return retval

let = raw_input('letters: ')
fin = open('words.txt')
for line in fin:
    l = line.strip()
    if uses_only(l,let):
        print l
