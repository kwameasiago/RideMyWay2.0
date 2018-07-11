from flask import Flask
from flask_restplus import Api
from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)
app.config.from_pyfile('../../config.py')
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app,version=2.0,title='Ride My Way')


from .user_views import *

api.add_resource(Signup,'/auth/signup')