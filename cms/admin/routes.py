from flask import Blueprint, render_template, request, Response, Flask, jsonify, session, g, redirect
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL
from ..system.config import SystemConfig, PERMISSION_MOD, PERMISSION_ADMIN, PERMISSION_MANAGER, PERMISSION_CEO

# App
app = Flask(__name__)

# Encrypt
bcrypt = Bcrypt(app)

# MySQL
mysql = MySQL()
mysql.init_app(app)
mysql = MySQL(app)

# Blueprint
mod = Blueprint('admin', __name__, template_folder='templates')

@mod.before_request
def before_request():
    if 'user_id' in session:
        # MySQL cursor
        db = mysql.connection.cursor()
        db.execute(f"SELECT id, username, mail, rank_class FROM users WHERE id = '{session['user_id']}'")
        result = db.fetchone()
        g.user = result
        
@mod.route('/')
def index():
    config = SystemConfig.load_configs()
    return render_template('index.html', config = config)