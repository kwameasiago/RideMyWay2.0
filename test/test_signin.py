import unittest
import json

from app.views.views import app
from .clean import delete_record


class TestSignIn(unittest.TestCase):
	"""
	class to test signin view
	"""
	def setUp(self):
		self.signup= {
		'first_name': 'test',
		'last_name': 'test',
		'email': 'testsignin@gmail.com',
		'user_type': 'driver',
		'password': 'test'
		}
		self.wrong_email = {
		'email': 'noteexist@gmail.com',
		'password': 'test'
		}
		self.wrong_password = {
		'email': 'testsignin@gmail.com',
		'password': 'notpassword'
		}
		self.valid_data = {
		'email': 'testsignin@gmail.com',
		'password': 'test'
		}
		self.content_type = 'Application/json'
		self.test = app.test_client()

	def tearDown(self):
		self.wrong_email = None
		self.wrong_password = None
		self.signup = None
		self.valid_data = None
		self.content_type = None
		self.test = None

	def test_invalid_email_status_Code(self):
		response = self.test.post('auth/login',content_type=self.content_type,
			data=json.dumps(self.wrong_email))
		self.assertEqual(response.status_code,405)

	def test_invalid_email_output(self):
		response = self.test.post('auth/login',content_type=self.content_type,
			data=json.dumps(self.wrong_email))
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(data['result'],'Email does not exist')

	def test_invalid_password_status_code(self):
		response = self.test.post('auth/signup',content_type=self.content_type,
			data=json.dumps(self.signup))
		response = self.test.post('auth/login',content_type=self.content_type,
			data=json.dumps(self.wrong_password))
		self.assertEqual(response.status_code,405)
		delete_record()

	def test_invalid_password_output(self):
		response = self.test.post('auth/signup',content_type=self.content_type,
			data=json.dumps(self.signup))
		response = self.test.post('auth/login',content_type=self.content_type,
			data=json.dumps(self.wrong_password))
		data = json.loads(response.get_data().decode("UTF-8"))
		self.assertEqual(data['result'],'Invalid password')
		delete_record()

	def test_valid_data_status_code(self):
		response = self.test.post('auth/signup',content_type=self.content_type,
			data=json.dumps(self.signup))
		response = self.test.post('auth/login',content_type=self.content_type,
			data=json.dumps(self.valid_data))
		self.assertEqual(response.status_code,200)
		delete_record()

	def test_valid_data_output(self):
		response1 = self.test.post('auth/signup',content_type=self.content_type,
			data=json.dumps(self.signup))
		response = self.test.post('auth/login',content_type=self.content_type,
			data=json.dumps(self.valid_data))
		data = json.loads(response.get_data().decode("UTF-8"))
		self.assertIn('Token',str(data))
		delete_record()

if __name__ == '__main__':
	unittest.main()