import unittest
import json

from app.views.views import app
from .clean import reset_db


class  UserTest(unittest.TestCase):
	"""
	class to test user signup
	"""
	def setUp(self):
		self.user_data= {
		'first_name': 'test',
		'last_name': 'test',
		'email': 'test@gmail.com',
		'user_type': 'driver',
		'password': 'test'
		}
		self.content_type = 'application/json'
		self.test = app.test_client()

	def tearDown(self):
		reset_db()
		self.user_data = None
		self.content_type = None
		self.test = None

	def test_signup_status_code(self):
		response = self.test.post('/auth/signup', data=json.dumps(self.user_data),content_type=self.content_type)
		self.assertEqual(201,response.status_code)

	def test_signup_output(self):
		response = self.test.post('/auth/signup', data=json.dumps(self.user_data),content_type=self.content_type)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual('Account created',data['result'])

	def test_email_exist_status_code(self):
		response = self.test.post('/auth/signup', data=json.dumps(self.user_data),content_type=self.content_type)
		response = self.test.post('/auth/signup', data=json.dumps(self.user_data),content_type=self.content_type)
		self.assertEqual(405,response.status_code)

	def test_email_exist_output(self):
		response = self.test.post('/auth/signup', data=json.dumps(self.user_data),content_type=self.content_type)
		response = self.test.post('/auth/signup', data=json.dumps(self.user_data),content_type=self.content_type)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual('Email exist',data['result'])


if __name__ == '__main__':
	unittest.main()