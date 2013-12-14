import os
from os import path
if not os.getenv("PYTHONPATH"):
	parent=os.path.split(os.path.realpath(__file__))[0] 
	os.putenv("PYTHONPATH",os.path.split(parent)[0])
import unittest
from sqlite import sql

class  TestSQLAgent(unittest.TestCase):

	def setup():
		self.conn=SQlAgent("./mydb.db")

	def test_creatDb():
		if self.conn.creatDb():
			assertNotEqual(self.conn,None)

	def test_getCursor():
		assertNotEqual(self.conn.getCursor(),None)

if __name__ == '__main__':
	
    unittest.main()
