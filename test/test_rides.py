import unittest
import json

from app.views.views import app
from .clean import delete_rides


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


class GetRideTest(unittest.TestCase):
	def setUp(self):
		self.test = app.test_client()
		self.content_type = 'Application/json'
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
		self.ride_data = {
		'date': '01-02-2018',
		'time': '12:00',
		'capacity': 3,
		'start': 'kahawa',
		'finish': 'mwiki'
		}
		reg_response = self.test.post('auth/signup',content_type=self.content_type,
			data=json.dumps(reg))
		response = self.test.post('auth/login',content_type=self.content_type,
			data=json.dumps(log))
		data = json.loads(response.get_data().decode('UTF-8'))
		token = data['Token']
		self.headers = {"X-API-KEY":"{}".format(token)}

	def tearDown(self):
		self.test =None
		self.content_type = None
		delete_rides()


	def test_get_all_rides(self):
		post = self.test.post('user/rides',content_type=self.content_type,
			data=json.dumps(self.ride_data),headers=self.headers)
		response = self.test.get('/rides',content_type=self.content_type,headers=self.headers)
		self.assertEqual(response.status_code,200)

	def test_get_one_ride(self):
		post = self.test.post('user/rides',content_type=self.content_type,
			data=json.dumps(self.ride_data),headers=self.headers)
		response = self.test.get('/rides/1',content_type=self.content_type,headers=self.headers)
		self.assertEqual(response.status_code,200)

	def test_get_one_none(self):
		post = self.test.post('user/rides',content_type=self.content_type,
			data=json.dumps(self.ride_data),headers=self.headers)
		response = self.test.get('/rides/-7',content_type=self.content_type,headers=self.headers)
		self.assertEqual(response.status_code,404)

	def test_get_one_none_output(self):
		post = self.test.post('user/rides',content_type=self.content_type,
			data=json.dumps(self.ride_data),headers=self.headers)
		response = self.test.get('/rides/-7',content_type=self.content_type,headers=self.headers)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(data['result'],'0 rides found')
