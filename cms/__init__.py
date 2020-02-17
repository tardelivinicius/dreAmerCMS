import os
from flask import Flask
from pathlib import Path
from dotenv import load_dotenv
from flask_mysqldb import MySQL
from cms.account.routes import mod
from cms.admin.routes import mod
from cms.login.routes import mod
from cms.register.routes import mod
from cms.system.config import mod
from cms.client.routes import mod
from cms.community.routes import mod

app = Flask(__name__)

# Secret Key
app.secret_key = os.getenv('SECRET_KEY')

# Enviroment
load_dotenv()
load_dotenv(dotenv_path='config.env')

# MySQL Config
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '030595'
app.config['MYSQL_DB'] = 'habbocms'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_UNIX_SOCKET'] = '127.0.0.1'
app.config['MYSQL_CONNECT_TIMEOUT'] = 3000
app.config['MYSQL_READ_DEFAULT_FILE'] = None
app.config['MYSQL_USE_UNICODE'] = True
app.config['MYSQL_CHARSET'] = None
app.config['MYSQL_SQL_MODE'] = None
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Routes
app.register_blueprint(account.routes.mod, url_prefix='/account')
app.register_blueprint(login.routes.mod)
app.register_blueprint(register.routes.mod, url_prefix='/register')
app.register_blueprint(system.config.mod)
app.register_blueprint(admin.routes.mod, url_prefix='/admin')
app.register_blueprint(client.routes.mod, url_prefix='/client')
app.register_blueprint(community.routes.mod, url_prefix='/community')