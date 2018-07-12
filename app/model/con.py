import psycopg2
from ..views.views import app
database = app.config['DATABASE_NAME']
password = app.config['PASSWORD']
user = app.config['USER']
host = app.config['HOST']

con = psycopg2.connect(dbname=database,password=password,host=host,user=user)