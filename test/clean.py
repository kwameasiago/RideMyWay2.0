from app.model.con import con


def delete_record(email):
	cur = con.cursor()
	sql = """
	DELETE FROM users WHERE EMAIL = '{}'
	""".format(email)
	cur.execute(sql)
	con.commit()