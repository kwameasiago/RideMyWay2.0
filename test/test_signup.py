import unittest
import json

from app.views.views import app


class  UserTest(unittest.TestCase):
	"""
	class to test user signup
	"""
	def setUp(self):
		self.user_data= {
		'first_name': 'john',
		'last_name': 'doe',
		'email': 'john@gmail.com',
		'user_type': 'driver',
		'password': 'password'
		}
		self.content_type = 'application/json'
		self.test = app.test_client()
		self.response = self.test.post('/auth/signup', data=json.dumps(self.user_data),content_type=self.content_type)
		self.data = json.loads(self.response.get_data().decode('UTF-8'))

	def tearDown(self):
		self.user_data = None
		self.content_type = None
		self.test = None

	def test_signup_status_code(self):
		self.assertEqual(201,self.response.status_code)

	def test_signup_output(self):
		self.assertEqual('Account created',self.data['result'])

	def test_email_exist_status_code(self):
		self.assertEqual(405,self.response.status_code)

	def test_email_exist_output(self):
		self.assertEqual('Email exist',self.data['result'])


if __name__ == '__main__':
	unittest.main()