import redis
import db_connections
import json
print 1111111111111111
import time
import datetime
import inspect
from db_constants import *


stocons = StorageConstants()

# r = db_connections.DbConnection().redis_db_connect()
# # r = redis.Redis(host= '104.155.181.214',port=6379,password='vh6HSwa9')
# print r
# data = {str(int(time.time())):datetime.datetime.now()}
# data = str(data)+','
# print data
# # r.delete('phone_time')
# # y = r.exists('phone_time')
# # if y:
# # 	r.append('phone_time',data)
# # else:
# # 	r.set('phone_time',data)
# print r.get('phone_time').split(',')
# print inspect.getmembers(db_connections.DbConnection(), predicate=inspect.ismethod)
# # redis_connection.close()


class StorageConnection(object):

	instances = 0

	def __init__(self,storage):
		self.instances = self.instances+1
		if 'redis' in storage:
			self.conn = db_connections.DbConnection().redis_db_connect()
		else:
			self.conn = db_connections.DbConnection().redis_db_connect()

	def dbops(self,key,value,operations):
		con = self.conn
		key = str(key)
		value = str(value)
		# if conn.exists(key) and 'update' in operations:
		if operations in [stocons.UPDATE,stocons.ADD]:
			conn.set(key,value)
		if operations in [APPEND]:
			if conn.exists(key):
				conn.append(key,value)
			else:
				conn.set(key,value)




