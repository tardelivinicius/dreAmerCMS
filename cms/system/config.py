from flask import Blueprint, Flask, g
from flask_mysqldb import MySQL

# App
app = Flask(__name__)

# MySQL
mysql = MySQL()
mysql.init_app(app)
mysql = MySQL(app)

# Blueprint
mod = Blueprint('system', __name__)

# Rank Permissions
PERMISSION_MOD = 6
PERMISSION_ADMIN = 7
PERMISSION_MANAGER = 8
PERMISSION_CEO = 9


class SystemConfig:

    def load_configs():
        # System Config
        db = mysql.connection.cursor()
        db.execute(''' SELECT * FROM cms_settings WHERE id = 1''')
        result = db.fetchone()

        # Users Online
        db = mysql.connection.cursor()
        db.execute(''' SELECT COUNT(*) as users_online FROM users WHERE online = '1' ''')
        users_online = db.fetchone()['users_online']

        result.update({'users_online': users_online})
        return result
