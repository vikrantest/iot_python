import sys
import redis
import db_constants
from pymongo import *
import psycopg2
import MySQLdb




cdef class DbConnection(object):


	def __init__(self):
		self.stocons = StorageConstants()


	def redis_db_connect(self,host=None,username=None,password=None,database=None):
		stocons = self.stocons
		_host = host or stocons.REDIS_DATABASE_HOST
		_password = password or stocons.REDIS_DATABASE_PASSWORD
		_database = database or 0
		_port = stocons.REDIS_PORT
		print _host,_port,_password

		try:
			if _password:
				print 444444444444444444444444444444444444444444444444433
				connection = redis.Redis(host= _host, port= _port, db= _database,password= 'vh6HSwa9')
			else:
				print 4444444333333333322222222222
				connection = redis.Redis(host= _host, port= _port, db= _database)
			return connection
		except:
			print "Error while connecting redis server db"
			return None



	def postgres_db_connect(self,host=None,username=None,password=None,database=None):
		_host = host or LOCALHOST
		_username = username
		_password = password
		_database = database

		try:
			connection = psycopg2.connect("host=_host,username=_username,password=_password,database=_database")
			return connection
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
			return None

	def mysql_db_connect(self,host=None,username=None,password=None,database=None):
		_host = host or LOCALHOST
		_username = username
		_password = password
		_database = database

		try:
			connection = MySQLdb.connect(_host,_username,_password,_database)
			return connection
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
			return None


	def mongo_db_connect(self,host=None,username=None,password=None,database=None,port=None):#check for username and password
		_host = host or LOCALHOST
		_database = database
		print port#None check
		if not port:
			_port = 27017
		url = '%s:%s' % (_host,port)

		try:
			if any([username is None,password is None ]):
				connection = MongoClient(url,connect=False)
			else:
				connection = MongoClient(url,username=username,password=password,connect=False)
			return connection
		except:
			print "Error while connecting mongo db"
			import sys
			print sys.exc_info()
			return None

		
	



