import logging
import sqlite3

#logging.basicConfig(filename='debug.log',level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',level=logging.DEBUG)

class SQLAgent(object):
	"""SqlAgent is a common interface to operate  sqlite3 database"""
	def __init__(self,name):
		super(SqlAgent, self).__init__()
		self._conn=None
		self._cursor=None
		self.name=name

	"""
	@param  name  the name of database
	@type string 
	@return connection object

	"""
	def createDb():
		self.conn=sqlite3.connect(self.name)
		if not self._conn:
			return  self._conn
		else:
			return None

	"""
	@return  get the cursor of the database
	"""
	def getCursor():
		self._cursor=self.conn.cursor()
		return self._cursor

	"""
	@param sql the sql want to execute
	@type string 
	@param  *args  the parameters in the sql string
	@type  list

	"""
	def _execute(sql,params):
		self._cursor.execute(sql,params)

	def _executemany(sql,params):
		self._cursor.executemany(sql,params)

	def commit():
		self._cursor.commit()

	def fetchone():
		return self._cursor.fetchone()

	def fetchmany():
		return self._cursor.fetchmany()

	def fetchall():
		return  self._cursor.fetchall()

	def  query(sqlstring,param):
		self._execute(sqlstring,param)

	def execute(sql,param):
		self._execute(sql,param)
		self.commit()
