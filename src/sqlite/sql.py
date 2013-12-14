import logging
import sqlite3

#logging.basicConfig(filename='debug.log',level=logging.DEBUG)
#logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',level=logging.DEBUG)

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
		logging.debug("start create database")
		if self._conn:
			return  self._conn
		else:
			logging.error("create database failed")
			raise Exception("create database error!")

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
	def _execute(self,sql,params=None):
		logging.debug( "------start execute-----")
		if self._cursor:
			logging.debug(sql)
			if params:
				self._cursor.execute(sql,params)
			else:
				logging.debug("params is none")
				logging.debug(sql)
				self._cursor.execute(sql)
		else:
			logging.debug("fail to execute sql:%s"%(sql))
			raise  ValueException("NoneType")

	def _executemany(self,sql,params):
		self._cursor.executemany(sql,params)

	def commit(self):
		if self._cursor:
			logging.debug("start to commit the operate")
			self._conn.commit()

	def fetchone(self):
		return self._cursor.fetchone()

	def fetchmany(self):
		return self._cursor.fetchmany()

	def fetchall(self):
		return  self._cursor.fetchall()

	def query(self,sql,param=None):
		self._execute(sql,param)

	def executeTable(self,sql,param=None):
		logging.debug("begin create  table")
		if param:
			self._execute(sql,param)
		else:
			self._execute(sql)


	def execute(self,sql,param=None):
		try:
			if param:
				logging.debug("start execute sql:%s:%s"%(sql,param))
				self._execute(sql,param)
			else:
				logging.debug("start execute sql:%s"%(sql))
				self._execute(sql)
			self.commit()
		except:
			raise  Exception('execute sql:%s failed'%(sql))

	def executemany(self,sql,params):
		try:
			if params:
				logging.debug("start execute sql:%s with params:%s"%(sql,params))
				self._executemany(sql,params)
			else:
				raise  Exception("params is None")
		except:
			pass
# def main():
# 	sa=SQLAgent("./mydb.db")
# 	sa.createDb()
# 	sa.getCursor()
# 	sql='''create table test(date text, trans text, symbol text, qty real, price real)'''
# 	sa.executeTable(sql)
# 	sql="""insert into test
#           values ('2006-01-05','BUY','RHAT',100,35.14)"""
# 	sa.execute(sql)

# if __name__ == '__main__':
# 		main()
