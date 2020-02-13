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

class SystemConfig:
    
    def __init__(self):
        self.cms_name = ''
        self.cms_client_limit = ''
        self.cms_maintenance = ''
        self.client_variables = ''
        self.client_texts = ''
        self.client_mus = ''
        self.client_ip = ''
        self.cms_url = ''
    

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