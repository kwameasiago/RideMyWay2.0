import jwt

from flask import request
from flask_restplus import Resource, fields

from .views import api,app
from .auth import *
from ..model.request import Request

Response_model = api.model('response',{
	'response':fields.String
	})


class PostRequest(Resource):
	@api.doc(security='Ride My Way')
	@token_required
	def post(self,rideId):
		token = jwt.decode(request.headers['X-API-KEY'],app.config['SECRET_KEY'])
		email = token['user']
		data = {'email':email,'request':'pending','rideId':rideId}
		ride_request = Request(data)
		return ride_request.send_request()


class GetAllRequest(Resource):
	@api.doc(security='Ride My Way')
	@token_required
	def get(self,rideId):
		return Request.get_all(rideId)

class Respond(Resource):
	@token_required
	@api.doc(security='Ride My Way')
	@api.expect(Response_model)
	def put(self,rideId,requestId):
		check=Request.check_response(requestId,rideId)
		if check is False:
			return {'result':'not found'},404
		else:
			data = request.get_json()
			if data['response'] == 'accept' or data['response'] == 'reject':
				return Request.respond(requestId,data['response'])
			else:
				return {'result':'Error expecting accept or reject'}