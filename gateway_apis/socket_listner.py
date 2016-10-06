#!/usr/bin/python

import socket
import sys
# import socket_config
import time
import db_ops


TCP_HOST = 'localhost'
TCP_PORT = 8040
CONNECTION_LIMIT = 10000


class MobileSocketListner(object):
	"""
	It will listen the port for data coming from mobile socket
	"""

	def __init__(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print "socket assigned"

	def connect_socket(self):
		try:self.socket.bind((TCP_HOST,DEFAULT_TCP_PORT))
		except:return "Socket connection not established"
		self.socket.listen(CONNECTION_LIMIT)
		print 'connection limit'
		self.conn, self.address = self.socket.accept()

		return "Connection established  ....................."

	def save_data(self,data):
		data = json.load(data)
		return True


	def socket_listner(self):
		self.connect_socket()
		print 'Looking for clients.............'

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






socket_obj = MobileSocketListner().socket_listner()





