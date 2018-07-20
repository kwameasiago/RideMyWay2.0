import unittest
import json

from app.views.views import app
from .clean import delete_rides, delete_request


class PostRequestTest(unittest.TestCase):
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
		token = data['Token']
		self.headers = {'X-API-KEY':'{}'.format(token)}
		


	def tearDown(self):
		self.test = None
		self.content_type = None
		self.headers = None
		delete_request()

	def test_post_request(self):
		response = self.test.post('/user/rides',content_type=self.content_type,
			data=json.dumps(self.ride_data), headers=self.headers)
		response = self.test.post('rides/1/request',content_type=self.content_type,
			headers=self.headers)
		self.assertEqual(response.status_code,201)

	def test_post_request_output(self):
		response = self.test.post('/user/rides',content_type=self.content_type,
			data=json.dumps(self.ride_data), headers=self.headers)
		response = self.test.post('rides/1/request',content_type=self.content_type,
			headers=self.headers)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(data['result'],'request sent')

	def test_get_request_output(self):
		response = self.test.post('/user/rides',content_type=self.content_type,
			data=json.dumps(self.ride_data), headers=self.headers)
		response = self.test.post('rides/1/request',content_type=self.content_type,
			headers=self.headers)
		response = self.test.get('/users/rides/1/requests',content_type=self.content_type,
			headers=self.headers)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,200)

	def test_put_request_output(self):
		response = self.test.post('/user/rides',content_type=self.content_type,
			data=json.dumps(self.ride_data), headers=self.headers)
		response = self.test.post('rides/1/request',content_type=self.content_type,
			headers=self.headers)
		response = self.test.put('/users/rides/1/requests/1',content_type=self.content_type,
			headers=self.headers, data=json.dumps({'response':'accept'}))
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,200)

	def test_put_request_output(self):
		response = self.test.post('/user/rides',content_type=self.content_type,
			data=json.dumps(self.ride_data), headers=self.headers)
		response = self.test.post('rides/1/request',content_type=self.content_type,
			headers=self.headers)
		response = self.test.put('/users/rides/1/requests/1',content_type=self.content_type,
			headers=self.headers, data=json.dumps({'response':'accept'}))
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(data['result'],'response sent')



