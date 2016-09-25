
#!python

import time
def test(int x):
	return x**2


def test_speed():
	print time.time()
	cdef a = 0
	for m in range(0,10000000):
		c = m*2
		d = c*2
		a+=m
	print time.time()
	return a


test(100)
test_speed()
print 11111111111111111111111111111111111111111111111111111111


# gcc $CFLAGS -I/usr/include/python2.7    -o test_server test_server.c -lpython2.7 -lpthread -lm -lutil -ldl
# cython test_server.py -o ../test_server.c --embed
