import psycopg2


database = 'ridemyway'
password = 'python'
user = 'postgres'

con = psycopg2.connect(dbname=database,password=password,host='localhost',user=user)