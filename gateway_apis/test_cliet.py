#!/usr/bin/env python

import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("localhost", 8040))

for index in xrange(500):
    data = "send data %d" % index
    print 'send to server: ' + data
    client_socket.send(data)
    while client_socket.recv(2048) != "ack":
        print "waiting for ack"
    print "ack received!"

#send disconnect message
dmsg = "disconnect"
print "Disconnecting"
client_socket.send(dmsg)

client_socket.close()