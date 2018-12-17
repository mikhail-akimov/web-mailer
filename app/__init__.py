from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['WTF_CSRF_SECRET_KEY'] = 'random key for form'
app.config['LDAP_PROTOCOL_VERSION'] = 3
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['LDAP_PROVIDER_URL'] = os.environ.get('LDAP_PROVIDER_URL')
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['SENDER'] = os.environ.get('SENDER')
app.config['COPY_GROUP'] = os.environ.get('COPY_GROUP')
app.config['BASE_DN'] = os.environ.get('BASE_DN')
app.config['FILTER_GROUP'] = os.environ.get('FILTER_GROUP')
app.config['DOMAIN'] = os.environ.get('DOMAIN')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

app.secret_key = 'some_random_key'

from app.auth.views import auth
from app.auth.models import *

app.register_blueprint(auth)

