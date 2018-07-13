from app.model.con import con


def reset_db():
	cur = con.cursor()
	sql = "DROP TABLE users;"
	cur.execute(sql)
	con.commit()