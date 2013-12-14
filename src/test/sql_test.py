import os
from os import path
if not os.getenv("PYTHONPATH"):
	parent=os.path.split(os.path.realpath(__file__))[0] 
	os.putenv("PYTHONPATH",os.path.split(parent)[0])
import unittest
from sqlite import sql

class  TestSQLAgent(unittest.TestCase):

	def setUp(self):
		self.db=sql.SQLAgent("./mydb.db")
		self.db.createDb()
		
	def tearDown(self):
		self.db=None
		os.remove("./mydb.db")

	def test_creatDb(self):
		if self.db:
			self.assertNotEqual(self.db.name,None)
			self.assertNotEqual(self.db.createDb(),None)
		else:
			self.assertTrue(False)

	def test_getCursor(self):
		if self.db:
			self.assertNotEqual(self.db.getCursor(),None)
		else:
			self.assertTrue(False)

		

if __name__ == '__main__':
	
    unittest.main()