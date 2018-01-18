'''
assignment-1
 This program the requests coming to virtual ip to one of the five real ips in
 round robin manner.
 To run the program from command line, enter the following:
  >>> assign1.py 10.0.0.6
  and press enter.
  Do this multiple time and you will see that the requests are mapping to real
  ips in round-robin manner. i.e.
  First time you type the above command on command line, you will get the
  output:
     connecting to 10.0.0.1
  Next time type the same command on command-line, you will get the output:
     connecting to 10.0.0.2
  and so on. Fifth time when you run the same command, you will get the output:
     connecting to 10.0.0.5
  and sixth time you will get the output:
     connecting to 10.0.0.1
  Thus, the output will be displayed in round-robin manner.
  ip.txt is used to store the intermediate values. Do not delete it.
'''

import sys

class loadbalancer:
	ip1 = '10.0.0.1'
	ip2 = '10.0.0.2'
	ip3 = '10.0.0.3'
	ip4 = '10.0.0.4'
	ip5 = '10.0.0.5'
	vip = '10.0.0.6'
	
	def vipconnect(self,ip):
		if ip == self.vip:
			f = open('ip.txt', 'r')
			k = int(f.read(1))
			if k==0:
				print 'connecting to ' + self.ip1
			elif k==1:
				print 'connecting to ' + self.ip2
			elif k==2:
				print 'connecting to ' + self.ip3
			elif k==3:
				print 'connecting to ' + self.ip4
			else:
				print 'connecting to ' + self.ip5			
			f.close()
			n = (k+1)%5
			f = open('ip.txt', 'w')
			f.write(str(n))
			f.close()
		else:
			print 'can\'t connect to ' + ip
	
lob = loadbalancer()
p = sys.argv[1]
lob.vipconnect(p)
