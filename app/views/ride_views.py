import jwt

from flask_restplus import Resource, fields
from flask import request

from .auth import *
from .views import api, app
from ..model.rides import Rides

ride_model = api.model('rides',{
	'date': fields.String,
	'time': fields.String,
	'capacity': fields.Integer,
	'start': fields.String,
	'finish': fields.String
	})

class PostRide(Resource):
	@token_required
	@api.expect(ride_model)
	@api.doc(security='Ride My Way')
	def post(self):
		token=jwt.decode(request.headers['X-API-KEY'],app.config['SECRET_KEY'])
		data = request.get_json()
		data['email']=token['user']
		rides = Rides(data)
		if rides.verify_data() is not False:
			return rides.verify_data()
		else:
			return rides.add_ride()
