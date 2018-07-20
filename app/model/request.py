import psycopg2

from .verifications import Verifications
from .con import con


class Request(Verifications):
	def __init__(self,data):
		self.data = data

	def user_id(self):
		try:
			sql="SELECT ID FROM users WHERE EMAIL='{}'".format(self.data['email'])
			cur=con.cursor()
			cur.execute(sql)
			user_id=cur.fetchone()
			return user_id[0]
		except psycopg2.Error as e:
			return {e.pgcode:e.pgerror}

	def create_table_request(self):
		try:
			sql="""
			CREATE TABLE IF NOT EXISTS request(
			ID SERIAL PRIMARY KEY,
			REQUEST VARCHAR(40) NOT NULL,
			RIDE_ID INT REFERENCES rides(ID),
			USER_ID INT REFERENCES users(ID)
			)
			"""
			cur = con.cursor()
			cur.execute(sql)
			con.commit()
		except psycopg2.Error as e:
			return {e.pgcode: e.pgerror}, 500

	def user_id(self):
		try:
			sql="SELECT ID FROM users WHERE EMAIL='{}'".format(self.data['email'])
			cur=con.cursor()
			cur.execute(sql)
			user_id=cur.fetchone()
			return user_id[0]
		except psycopg2.Error as e:
			return {e.pgcode:e.pgerror}

	def ride_id(self,rideId):
		try:
			sql = "SELECT ID FROM rides WHERE ID={}".format(rideId)
			cur =con.cursor()
			cur.execute(sql)
			item = cur.fetchone()
			if item is None:
				return False
			else:
				return item
		except psycopg.Error as e:
			return {e.pgcode:e.pgerror}

	def send_request(self):
		self.create_table_request()
		if self.ride_id(self.data['rideId']) is False:
			return {'result': 'invalid id'}, 405
		try:
			sql="""
			INSERT INTO request(REQUEST,RIDE_ID,USER_ID)
			VALUES('{}',{},{})
			""".format(self.data['request'],self.data['rideId'],self.user_id())
			cur = con.cursor()
			cur.execute(sql)
			con.commit()
			return {'result':'request sent'}, 201
		except psycopg2.Error as e:
			return {e.pgcode:e.pgerror}

	@classmethod
	def get_all(cls,rideId):
		try:
			request = []
			sql = "SELECT ID,REQUEST,RIDE_ID,USER_ID FROM request WHERE RIDE_ID={};".format(rideId)
			cur = con.cursor()
			cur.execute(sql)
			items = cur.fetchall()
			for item in items:
				request.append({
					'id':item[0],
					'request':item[1],
					'ride_id': item[2],
					'user_id': item[3]
					})
			if len(request) == 0:
				return {'result': 'not found'},404
			else:
				return request
		except psycopg2.Error as e:
			return {e.pgcode:e.pgerror}

	@classmethod
	def check_response(cls,requestId,rideId):
		requestId, rideId = int(requestId),int(rideId)
		try:
			sql = "SELECT RIDE_ID, ID FROM request WHERE RIDE_ID={} AND ID={}".format(rideId,requestId)
			cur =con.cursor()
			cur.execute(sql)
			item = cur.fetchall()
			if len(item) == 0:
				return False
			else:
				return item
		except psycopg2.Error as e:
			return {e.pgcode:r.pgerror}

	@classmethod
	def respond(cls,requestId,request):
		try:
			sql = "UPDATE request SET REQUEST ='{}' WHERE ID={}".format(request,int(requestId))
			cur=con.cursor()
			cur.execute(sql)
			con.commit()
			return {'result': 'response sent'}
		except psycopg2.Error as e:
			con.rollback()
			return {e.pgcode:e.pgerror}
