from app.model.con import con


def delete_record():
	try:
		cur = con.cursor()
		sql = "TRUNCATE users CASCADE;"
		cur.execute(sql)
		con.commit()
	except:
		con.rollback()