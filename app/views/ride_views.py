from flask_restplus import Resource

from .auth import *
from .views import app,api

class PostRide(Resource):
	@token_required
	@api.doc(security='X-API-KEY')
	def post(self):
		return {'result': 'testing'}
