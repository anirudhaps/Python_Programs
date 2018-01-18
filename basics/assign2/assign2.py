# program to map the requests coming to virtual ip to one of the real ips in
# such a way that 50% requests map to
# ip1, 25% map to ip2, and the rest 25% map to ip3
import math

def maptoIP(n,lst):
	k = n/2.0
	f = math.floor(k)
	r = k-f
	if r>=0.5:
		ln = math.ceil(k)
	else:
		ln = f
	i=0
	while i<ln:
		print 'Host %d is connected to %s' % (i+1,lst[1])
		i = i+1
	ns = n-ln
	nk = ns/2.0
	fk = math.floor(nk)
	rk = nk-fk
	if rk>=0.5:
		lnk = math.ceil(nk)
	else:
		lnk = fk
	j=0
	while j<lnk:
		print 'Host %d is connected to %s' % (j+ln+1, lst[2])
		j = j+1
	last = n-(ln+lnk)
	q = 0
	while q<last:
		print 'Host %d is connected to %s' % (q+ln+lnk+1,lst[3])
		q = q+1

lt = ['10.0.0.4', '10.0.0.1', '10.0.0.2', '10.0.0.3']
n = input('Enter the number of requests: ')
print 'Trying to connect to ' + lt[0]
maptoIP(n,lt)
