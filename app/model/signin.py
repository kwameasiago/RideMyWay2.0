import psycopg2
from werkzeug.security import check_password_hash

from .verifications import Verifications
from .con import con


class Login(Verifications):
	def __init__(self,data):
		self.string_list = [data['email'],data['password']]
		self.data=data
		self.empty_data = Verifications.empty_data(self,self.string_list)
		self.whitespace_data = Verifications.whitespace_data(self,self.string_list)
		self.email_data = Verifications.email_data(self,self.data['email'])


	def verify_data(self):
		if self.empty_data is not False:
			return self.empty_data
		elif self.whitespace_data is not False:
			return self.whitespace_data
		elif self.email_data is not False:
			return self.email_data
		else:
			return False

	def login(self,token):
		try:
			cur = con.cursor()
			sql = "SELECT password FROM users WHERE email = '{}'".format(self.data['email'])
			cur.execute(sql)
			item = cur.fetchone()
			if item is None:
				return {'result': 'Email does not exist'},405
			else:
				if check_password_hash(item[0],self.data['password']) is True:
					return {'Token': token}
				else:
					return {'result':'Invalid password'},405
		except psycopg2.Error as e:
			return {e.pgcode:e.pgerror}
