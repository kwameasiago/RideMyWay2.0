from app.model.con import con


def delete_record():
	try:
		cur = con.cursor()
		sql = "DROP TABLE users;"
		cur.execute(sql)
		con.commit()
	except:
		con.rollback()

def delete_rides():
	try:
		cur = con.cursor()
		sql = "DROP TABLE rides;"
		cur.execute(sql)
		con.commit()
	except:
		con.rollback()

def delete_request():
	try:
		cur = con.cursor()
		sql = "DROP TABLE request;"
		cur.execute(sql)
		con.commit()
	except:
		con.rollback()