import sys
import redis
import db_constants




cdef class DbConnection(object):


	def redis_db_connect(self,host=None,username=None,password=None,database=None):
		_host = host or db_constants.REDIS_DATABASE_HOST
		_password = password or db_constants.REDIS_DATABASE_PASSWORD
		_database = database or 0
		_port=db_constants.REDIS_PORT
		print _host,_port,_password

		try:
			if password:
				connection = redis.Redis(host= _host, port= _port, db= _database,password= _password)
			else:
				connection = redis.Redis(host= _host, port= _port, db= _database)
			return connection
		except:
			print "Error while connecting redis server db"
			return None


		return True

		
	



