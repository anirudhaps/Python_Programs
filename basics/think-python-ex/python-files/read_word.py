'''
Write a program that reads words.txt and prints only the words with more than 20
characters (not counting whitespace).
'''

fin = open('words.txt')
for line in fin:
    l = line.strip()
    if len(l)>20:
        print l
        
