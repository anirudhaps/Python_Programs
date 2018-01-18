'''
Writing in file: python learning
'''

fout = open('newfile.txt','w')
line = 'Hi, I am Anirudha.\n'
fout.write(line)
line = 'I am persuing M.Tech in IT.\n'
fout.write(line)
v = 25
fout.write(str(v) + '\n')
fout.write(('%d' % 40) + '\n')
fout.write('Array: %d %d %d %d' % (1,2,3,4) + '\n')
fout.close()
