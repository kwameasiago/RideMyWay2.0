from .verifications import Verifications
from .con import con


class Register(Verifications):
	def __init__(self,data):
		self.string_list = [
		data['first_name'],data['last_name'],
		data['email'],data['user_type'],data['password']
		]
		self.empty_data = Verifications.empty_data(self, self.string_list)
		self.whitespace_data = Verifications.whitespace_data(self, self.string_list)
		self.email_data = Verifications.email_data(self, data['email'])
		self.user_type = Verifications.user_type(self, data['user_type'])

	def verify_data(self):
		if self.empty_data is not False:
			return self.empty_data
		elif self.whitespace_data is not False:
			return self.whitespace_data
		elif self.email_data is not False:
			return self.email_data
		elif self.user_type is not False:
			return self.user_type
		else:
			return False

	def insert_data(self):
		pass

