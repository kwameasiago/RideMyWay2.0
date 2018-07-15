import psycopg2

from .verifications import Verifications
from .con import con

class Rides(Verifications):
	def __init__(self,data):
		self.string_list=[
		data['start'],data['time'],
		data['finish'],data['date']]
		self.empty_data = Verifications.empty_data(self,self.string_list)
		self.whitespace_data = Verifications.whitespace_data(self,self.string_list)
		self.data=data

	def verify_data(self):
		if self.whitespace_data is not False:
			return self.whitespace_data
		elif self.empty_data is not False:
			return self.empty_data
		else:
			return False

	def create_table_rides(self):
		try:
			sql="""
			CREATE TABLE IF NOT EXISTS rides(
			ID SERIAL PRIMARY KEY,
			START VARCHAR(50) NOT NULL,
			FINISH VARCHAR(50) NOT NULL,
			DEP_DATE VARCHAR(50) NOT NULL,
			CAPACITY INT NOT NULL,
			USER_ID INT REFERENCEs users(ID));
			"""
			cur = con.cursor()
			cur.execute(sql)
			con.commit()
			return {'result': 'ok'}
		except psycopg2.Error as e:
			con.rollback()
			return {e.pgcode:e.pgerror},500

	def user_id(self):
		try:
			sql="SELECT ID FROM users WHERE EMAIL='{}'".format(self.data['email'])
			cur=con.cursor()
			cur.execute(sql)
			user_id=cur.fetchone()
			return user_id[0]
		except psycopg2.Error as e:
			return {e.pgcode:e.pgerror}

	def add_ride(self):
		self.create_table_rides()
		try:
			sql="""
			INSERT INTO rides
			(START,FINISH,DEP_DATE,CAPACITY,USER_ID) VALUES
			('{}','{}','{}',{},{});""".format(
				self.data['start'],self.data['finish'],
				self.data['date'],self.data['capacity'],
				self.user_id())
			cur = con.cursor()
			cur.execute(sql)
			con.commit()
			return{'result': 'Ride posted'},201
		except psycopg2.Error as e:
			con.rollback()
			return {e.pgcode:e.pgerror}