import psycopg2
from werkzeug.security import generate_password_hash

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
		self.data = data

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

	def create_table_users(self):
		try:
			cur = con.cursor()
			sql = """
			CREATE TABLE IF NOT EXISTS users(
			ID SERIAL PRIMARY KEY,
			FIRST_NAME VARCHAR(50) NOT NULL,
			LAST_NAME VARCHAR(60) NOT NULL,
			EMAIL VARCHAR(80) NOT NULL,
			USER_TYPE VARCHAR(50) NOT NULL,
			PASSWORD VARCHAR(90) NOT NULL
			)
			"""
			cur.execute(sql)
			con.commit()
		except psycopg2.Error as e:
			return{e.pgcode:e.pgerror}, 500

	def email_exist(self):
		self.create_table_users()
		try:
			cur = con.cursor()
			sql = """
			SELECT EMAIL FROM users WHERE EMAIL='{}';
			""".format(self.data['email'])
			cur.execute(sql)
			item = cur.fetchone()
			if item is not None:
				return True
		except psycopg2.Error as e:
			return{e.pgcode:e.pgerror}, 500

	def insert_data(self):
		password = generate_password_hash(self.data['password'],method='sha256')
		try:
			cur = con.cursor()
			sql = """
			INSERT INTO users(FIRST_NAME,LAST_NAME,EMAIL,USER_TYPE,PASSWORD) 
			VALUES('{}','{}','{}','{}','{}')""".format(self.data['first_name'],self.data['last_name'],
				self.data['email'],self.data['user_type'],password)
			cur.execute(sql)
			con.commit()
			return{'result':'Account created'},201
		except psycopg2.Error as e:
			return{e.pgcode:e.pgerror}
