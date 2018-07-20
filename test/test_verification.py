import unittest
import json

from app.views.views import app


class  VerificationTest(unittest.TestCase):
	"""
	class to test verifications
	"""
	def setUp(self):
		self.empty_data= {
		'first_name': '',
		'last_name': 'doe',
		'email': 'john@gmail.com',
		'user_type': 'driver',
		'password': 'password'
		}
		self.whitespace_data= {
		'first_name': '  ',
		'last_name': 'doe',
		'email': 'john@gmail.com',
		'user_type': 'driver',
		'password': 'password'
		}
		self.email_data= {
		'first_name': 'john',
		'last_name': 'doe',
		'email': 'johngmail.com',
		'user_type': 'driver',
		'password': 'password'
		}
		self.user_type= {
		'first_name': 'john',
		'last_name': 'doe',
		'email': 'john@gmail.com',
		'user_type': 'cow',
		'password': 'password'
		}
		self.content_type = 'application/json'
		self.test = app.test_client()

	def tearDown(self):
		self.user_data = None
		self.content_type = None
		self.test = None

	def test_empty_data_status_code(self):
		response = self.test.post('/auth/signup', data=json.dumps(self.empty_data),content_type=self.content_type)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEquals(response.status_code,405)

	def test_empty_data_output(self):
		response = self.test.post('/auth/signup', data=json.dumps(self.empty_data),content_type=self.content_type)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(data['result'],'Invalid input(Empty data)')

	def test_whitespace_data_status_code(self):
		response = self.test.post('/auth/signup', data=json.dumps(self.whitespace_data),content_type=self.content_type)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEquals(response.status_code,405)

	def test_whitespace_data_output(self):
		response = self.test.post('/auth/signup', data=json.dumps(self.whitespace_data),content_type=self.content_type)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(data['result'],'Invalid input(Whitespace data)')

	def test_email_status_code(self):
		response = self.test.post('/auth/signup', data=json.dumps(self.email_data),content_type=self.content_type)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEquals(response.status_code,405)

	def test_email_output(self):
		response = self.test.post('/auth/signup', data=json.dumps(self.email_data),content_type=self.content_type)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(data['result'],'Invalid email')

	def test_user_type_status_code(self):
		response = self.test.post('/auth/signup', data=json.dumps(self.user_type),content_type=self.content_type)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,405)

	def test_user_type_output(self):
		response = self.test.post('/auth/signup', data=json.dumps(self.user_type),content_type=self.content_type)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(data['result'],'Invalid input (expecting driver or rider)')
