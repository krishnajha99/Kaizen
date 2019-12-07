import json
import unittest
from main import app

class TestMyApp(unittest.TestCase):
	def setUp(self):
		self.app = app
		self.client = self.app.test_client()
	def test_index(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code,200)
	def test_home(self):
		resp = self.client.get('/home')
		self.assertEqual(resp.status_code,200)
	def test_home_post(self):
		resp = self.client.post(path="/home",data = 'MSFT')
		self.assertEqual(resp.status_code,200)

if __name__=='__main__':
	unittest.main()
		
