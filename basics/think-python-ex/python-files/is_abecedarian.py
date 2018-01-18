'''
Exercise 9-6
'''

def is_abecedarian(word):
    prev_letter = word[0]
    i=1
    while i<len(word):
        ascii_prev_letter = ord(prev_letter)
        if ord(word[i])<ascii_prev_letter:
            return False
        prev_letter = word[i]
        i+=1
    return True

w = raw_input('Enter any word: ')
print 'is_abecedarian?:', is_abecedarian(w)
