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
        db = mysql.connection.cursor()
        db.execute(''' SELECT * FROM cms_settings ORDER BY id ASC''')
        result = db.fetchall()

        configs = {
            "cms_name": result[0]['value'],
            "cms_url": result[1]['value'],
            "cms_client_limit": result[2]['value'],
            "cms_maintenance": result[3]['value'],
            "client_ip": result[4]['value'],
            "client_mus": result[5]['value'],
            "client_texts": result[6]['value'],
            "client_variables": result[7]['value'],
            "register_enable": result[8]['value']
        }

        return configs