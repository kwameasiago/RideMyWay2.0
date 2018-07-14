from flask import request
from functools import wraps

def token_required(f):
	@wraps(f)
	def decorated(*args,**kwargs):
		token = None
		if 'X-API-KEY' in request.headers:
			token = request.headers['X-API-KEY']
		if not token:
			return {'result': 'Token is missing'}, 405

		try:
			data = jwt.decode(token,app.config['SECRET_KEY'])
		except:
			return {'result': 'Token is invalid'}, 405

		return f(*args,**kwargs)

	return decorated