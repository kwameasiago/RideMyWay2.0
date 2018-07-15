import unittest
import json

from app.views.views import app


class PostRideTest(unittest.TestCase):
	def setUp(self):
		self.test = app.test_client()
		self.content_type = 'Application/json'
		self.ride_data = {
		'date': '01-02-2018',
		'time': '12:00',
		'capacity': 3,
		'start': 'kahawa',
		'finish': 'mwiki'
		}
		self.bad_token ={'X-API-KEY':'not token'}
		reg = {
		'first_name': 'test',
		'last_name': 'test',
		'email': 'test@gmail.com',
		'user_type': 'driver',
		'password': 'test'
		}
		log = {
		'email': 'test@gmail.com',
		'password': 'test'
		}
		reg_response = self.test.post('auth/signup',content_type=self.content_type,
			data=json.dumps(reg))
		response = self.test.post('auth/login',content_type=self.content_type,
			data=json.dumps(log))
		data = json.loads(response.get_data().decode('UTF-8'))
		self.token = data['Token']
		


	def tearDown(self):
		self.test = None
		self.content_type = None
		self.headers = None

	def test_no_token_status_code(self):
		response = self.test.post('/user/rides',content_type=self.content_type,
			data=json.dumps(self.ride_data))
		self.assertEqual(response.status_code,405)

	def test_no_token_output(self):
		response = self.test.post('user/rides',content_type=self.content_type,
			data=json.dumps(self.ride_data))
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(data['result'],'Token is missing')

	def test_invalid_token_status_code(self):
		response = self.test.post('user/rides',content_type=self.content_type,
			data=json.dumps(self.ride_data),headers=self.bad_token)
		self.assertEqual(response.status_code,405)

	def test_invalid_token_output(self):
		response = self.test.post('user/rides',content_type=self.content_type,
			data=json.dumps(self.ride_data),headers=self.bad_token)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(data['result'],'Token is invalid')

	def test_valid_ride_output(self):
		headers = {"X-API-KEY":"{}".format(self.token)}
		response = self.test.post('user/rides',content_type=self.content_type,
			data=json.dumps(self.ride_data),headers=headers)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(data['result'],'Ride posted')

	def test_valid_ride_status_code(self):
		headers = {"X-API-KEY":"{}".format(self.token)}
		response = self.test.post('user/rides',content_type=self.content_type,
			data=json.dumps(self.ride_data),headers=headers)
		self.assertEqual(response.status_code,201)