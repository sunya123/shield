import logging
import sqlite3

#logging.basicConfig(filename='debug.log',level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',level=logging.DEBUG)

class SQLAgent(object):
	"""SqlAgent is a common interface to operate  sqlite3 database"""
	def __init__(self,name):
		super(SQLAgent, self).__init__()
		self._conn=None
		self._cursor=None
		self.name=name

	"""
	@param  name  the name of database
	@type string 
	@return connection object

	"""
	def createDb(self):
		self._conn=sqlite3.connect(self.name)
		logging.debug("create database")
		if self._conn:
			return  self._conn
		else:
			logging.error("create database failed")
			return None

	"""
	@return  get the cursor of the database
	"""
	def getCursor(self):
		if self._conn:
			self._cursor=self._conn.cursor()
			return self._cursor
		else:
			raise Exception("NoneType to use")

	"""
	@param sql the sql want to execute
	@type string 
	@param  *args  the parameters in the sql string
	@type  list

	"""
	def _execute(self,sql,params):
		self._cursor.execute(sql,params)

	def _executemany(self,sql,params):
		self._cursor.executemany(sql,params)

	def commit(self):
		self._cursor.commit()

	def fetchone(self):
		return self._cursor.fetchone()

	def fetchmany(self):
		return self._cursor.fetchmany()

	def fetchall(self):
		return  self._cursor.fetchall()

	def  query(self,sqlstring,param):
		self._execute(sqlstring,param)

	def execute(self,sql,param):
		self._execute(sql,param)
		self.commit()

