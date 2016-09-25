#!/usr/bin/python

import socket
import sys
# import socket_config
import time
import db_ops


TCP_HOST = 'localhost'
DEFAULT_TCP_PORT = 8040
SECONDRY_TCP_PORT = 8045
CONNECTION_LIMIT = 10000

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind((TCP_HOST,SECONDRY_TCP_PORT))
# server_socket.listen(5)

# print "Listening for client . . ."
# print 'wait....'
# conn, address = server_socket.accept()
# print "Connected to client at  - ", address
# current_time = int(time.time())
# #pick a large output buffer size because i dont necessarily know how big the incoming packet is                                                    
# while current_time+10>int(time.time()):
# 	output = conn.recv(2048);
# 	if output.strip() == "disconnect":
# 		conn.close()
# 		sys.exit("Received disconnect message.  Shutting down.")
# 		conn.send("dack")
# 	elif output:
# 		print "Message received from client:"
# 		print output
# 		conn.send("ack")

class MobileSocketListner(object):
	"""
	It will listen the port for data coming from mobile socket
	"""

	def __init__(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print "socket assigned"

	def connect_socket(self):
		try:self.socket.bind((TCP_HOST,DEFAULT_TCP_PORT))
		except:
			try:self.socket.bind((TCP_HOST,SECONDRY_TCP_PORT))
			except:return "Socket connection not established"
		self.socket.listen(CONNECTION_LIMIT)
		print 'connection limit'
		self.conn, self.address = self.socket.accept()
		print 'hereeeeeeeeeeeeee'

		return "Connection established , listening for clients ....................."


	def socket_listner(self):
		self.connect_socket()
		print 'waiting for clients.............'

		current_time = int(time.time())

		while current_time+10>int(time.time()):
			data = self.conn.recv(4096)
			if 'disconnect' in data.strip():
				self.conn.close()
				sys.exit('Shutting down TCP connection.')
				self.conn.send('close acknowledge')
			else:
				print data

				self.conn.send('ack')

	def save_data(self,data):
		data = json.load(data)
		return True




socket_obj = MobileSocketListner().socket_listner()





