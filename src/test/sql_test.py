import os
import logging
from os import path
if not os.getenv("PYTHONPATH"):
	parent=os.path.split(os.path.realpath(__file__))[0] 
	os.putenv("PYTHONPATH",os.path.split(parent)[0])
import unittest
from sqlite import sql

logging.basicConfig(format='%(asctime)s %(funcName)s %(levelname)s:%(message)s',level=logging.DEBUG)

class  TestSQLAgent(unittest.TestCase):

	def setUp(self):
		self.agent=sql.SQLAgent("./mydb.db")

	def tearDown(self):
		self.agent=None
		os.remove("./mydb.db")

	def test_creatDb(self):
		if self.agent:
			self.agent.createDb()
			self.assertNotEqual(self.agent.name,None)
			self.assertNotEqual(self.agent.createDb(),None)
		else:
			self.assertTrue(False)

	def test_getCursor(self):
		if self.agent:
			self.agent.createDb()
			self.assertNotEqual(self.agent.getCursor(),None)
		else:
			self.assertTrue(False)

	def test_createTable(self):
		if self.agent:
			sql='''create table test
                 (date text, trans text, symbol text,
                    qty real, price real)'''
			self.agent.createDb()
			self.agent.getCursor()
			self.agent.executeTable(sql)
			sql="drop table test"
			self.agent.executeTable(sql)

	def test_execute(self):
		if self.agent:
			self.agent.createDb()
			self.agent.getCursor()
			sql='''create table test
                 (date text, trans text, symbol text,
                    qty real, price real)'''

			self.agent.executeTable(sql)
			sql="""insert into test values ('2006-01-05','BUY','RHAT',100,35.14)"""
			self.agent.execute(sql)
			sql='insert into test values(?,?,?,?,?)'
			param=('2006-01-07','SALE','RH',10,30.14)
			self.agent.execute(sql,param)
		else:
			self.assertTrue(False)


		

if __name__ == '__main__':
	
    unittest.main()