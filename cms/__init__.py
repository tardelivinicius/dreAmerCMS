from flask import Flask
from flask_mysqldb import MySQL
from cms.account.routes import mod
from cms.login.routes import mod
from cms.register.routes import mod
from cms.system.config import mod
from cms.admin.routes import mod


app = Flask(__name__)
app.secret_key = 'grWvcvaRu3YXHH22KLncM893c8IV1d5d'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '030595'
app.config['MYSQL_DB'] = 'habbelixcms'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_UNIX_SOCKET'] = '127.0.0.1'
app.config['MYSQL_CONNECT_TIMEOUT'] = 3000
app.config['MYSQL_READ_DEFAULT_FILE'] = ''
app.config['MYSQL_USE_UNICODE'] = True
app.config['MYSQL_CHARSET'] = ''
app.config['MYSQL_SQL_MODE'] = None
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


app.register_blueprint(account.routes.mod, url_prefix='/account')
app.register_blueprint(login.routes.mod)
app.register_blueprint(register.routes.mod, url_prefix='/register')
app.register_blueprint(system.config.mod)
app.register_blueprint(admin.routes.mod, url_prefix='/admin')