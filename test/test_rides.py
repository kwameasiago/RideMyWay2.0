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
		self.bad_headers ={'X-API-KEY':'not token'}

	def tearDown(self):
		self.test = None
		self.content_type = None

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
			data=json.dumps(self.ride_data),headers=self.bad_headers)
		self.assertEqual(response.status_code,405)

	def test_invalid_token_output(self):
		response = self.test.post('user/rides',content_type=self.content_type,
			data=json.dumps(self.ride_data),headers=self.bad_headers)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(data['result'],'Token is invalid')

	def test_valid_ride_output(self):
		response = self.test.post('user/rides',content_type=self.content_type,
			data=json.dumps(self.ride_data))
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(data['result'],'Ride posted')

	def test_valid_ride_status_code(self):
		response = self.test.post('user/rides',content_type=self.content_type,
			data=json.dumps(self.ride_data))
		self.assertEqual(response.status_code,201)