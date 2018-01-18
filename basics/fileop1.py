# file reading and writing

file1 = open('e:/python/f1.txt','w')
# the above statement will create an empty file named as f1.txt
# If f1.txt already exists, then this statement will delete all the contents of
# f1.txt leading to an empty file.
# If we try to open a new file(i.e. the one which is not already created) in
# read(r) mode, then it is an error

file1.write('Summer is started.\nI am fealing hot in afternoon.')
file1.write('It\'s OK. I will switch on fan.')
file1.close() # on calling this function, the content will be written in the
# file f1.txt

fob=open('e:/python/f1.txt','r')
print fob.read(3) # reads first three bytes from file
print fob.read(1) # reads next 1 byte
print fob.read()  # reads remaining content of the file
fob.close()
