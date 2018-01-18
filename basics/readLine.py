# reading lines from a file

fob = open('e:/python/f1.txt','r')
lst = fob.readlines()
fob.close()

for l in lst:
    print l

# fob.readline() reads a single line at a time
# fob.readlines() reads all the lines in a single go and returns a list of them
