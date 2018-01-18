# modifying lines in a file

fob = open('e:/python/f1.txt','r')
lst = fob.readlines()
print lst
fob.close()

lst[2] = "It's OK. I'll manage.\n"
fob = open('e:/python/f1.txt','w')
fob.writelines(lst)
fob.close()
