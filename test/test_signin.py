import unittest
import json

from app.views.views import app


class TestSignIn(unittest.TestCase):
	"""
	class to test signin view
	"""
	def setUp(self):
		self.wrong_email = {
		'email': 'noteexist@gmail.com',
		'password': 'password'
		}
		self.wrong_password = {
		'email': 'johndoe@gmail.com',
		'password': 'notpassword'
		}
		self.valid_data = {
		'email': 'noteexist@gmail.com',
		'password': 'password'
		}
		self.content_type = 'Application/json'
		self.test = app.test_client()

	def tearDown(self):
		self.wrong_email = None
		self.content_type = None
		self.test = app.test_client()

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
		response = self.test.post('auth/login',content_type=self.content_type,
			data=json.dumps(self.wrong_password))
		self.assertEqual(response.status_code,405)

	def test_invalid_password_output(self):
		response = self.test.post('auth/login',content_type=self.content_type,
			data=json.dumps(self.wrong_password))
		data = json.loads(response.get_data().decode("UTF-8"))
		self.assertEqual(data['result'],'Invalid password')

	def test_valid_data_status_code(self):
		response = self.test.post('auth/login',content_type=self.content_type,
			data=json.dumps(self.valid_data))
		self.assertEqual(response.status_code,200)

	def test_valid_data_output(self):
		response = self.test.post('auth/login',content_type=self.content_type,
			data=json.dumps(self.valid_data))
		data = json.loads(response.get_data().decode("UTF-8"))
		self.assertEqual(data['result'],'ok')
