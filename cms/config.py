from flask_mysqldb import MySQL

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '030595'
app.config['MYSQL_DB'] = 'davidaulas'
app.config['MYSQL_CURSORCLASS'] = 'Dict'

mysql = MySQL()
mysql.init_app(app)