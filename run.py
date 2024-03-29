import os
from flask import Flask, app
from dotenv import load_dotenv
from flask_mysqldb import MySQL
from cms.account.controllers import account
from cms.admin.controllers import admin
from cms.login.controllers import system_login
from cms.register.controllers import register
from cms.system.config import system
from cms.client.controllers import system_client
from cms.community.controllers import community

app = Flask(__name__)

# Secret Key
app.secret_key = '1284721412AKJSDHADHDJOSH'

# # Enviroment
project_folder = os.path.expanduser('~/dreamercms')
load_dotenv(os.path.join(project_folder, '.env'))

# MySQL Config
app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST")
app.config['MYSQL_USER'] = os.getenv("MYSQL_USER")
app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
app.config['MYSQL_DB'] = os.getenv("MYSQL_DB")
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_UNIX_SOCKET'] = ''
app.config['MYSQL_CONNECT_TIMEOUT'] = 3000
app.config['MYSQL_READ_DEFAULT_FILE'] = None
app.config['MYSQL_USE_UNICODE'] = True
app.config['MYSQL_CHARSET'] = None
app.config['MYSQL_SQL_MODE'] = None
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['FLASK_ENV'] = 'development'

# Routes
app.register_blueprint(account, url_prefix='/account')
app.register_blueprint(system_login)
app.register_blueprint(register, url_prefix='/register')
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(system_client, url_prefix='/client')
app.register_blueprint(community, url_prefix='/community')
