'''
Exercise 10-10
'''
import time

def build_list_V1():
    fn = open('words.txt')
    out = []
    for w in fn:
        word = w.strip()
        out.append(word)
    return out


def build_list_V2():
    fn = open('words.txt')
    out = []
    for w in fn:
        word = w.strip()
        out = out + [word]
    return out
    

#start = time.time()
#build_list_V1()
#elapsed_time = time.time() - start
#print 'elapsed time for V1: ' + str(elapsed_time) 

#start = time.time()
#build_list_V2()  # takes more time than version-1
#elapsed_time = time.time() - start
#print 'elapsed time for V2: ' + str(elapsed_time) 
