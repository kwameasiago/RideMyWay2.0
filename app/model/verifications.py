import re

class Verifications:
	"""
	class to verify data before inserting to database
	"""
	def __init__(self):
		self.data_err = None

	def empty_data(self,items):
		for item in items:
			if not item:
				return {'result': 'Invalid input(Empty data)'}, 405
		return False

	def whitespace_data(self,items):
		for item in items:
			if item.isspace() is True:
				self.data_err = {'result': 'Invalid input(Whitespace data)'}, 405
				return self.data_err
		return False

	def email_data(self,email):
		result = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
		if result is None:
			self.data_err = {'result': 'Invalid email'}, 405
			return self.data_err
		else:
			return False

	def user_type(self,user_type):
		if user_type == 'driver' or user_type == 'rider':
			return False
		else:
			self.data_err = {'result': 'Invalid input (expecting driver or rider)'}, 405
			return self.data_err
