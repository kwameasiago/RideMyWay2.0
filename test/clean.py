from app.model.con import con


def delete_record():
	try:
		cur = con.cursor()
		sql = "DELETE FROM users;"
		cur.execute(sql)
		con.commit()
	except:
		con.rollback()