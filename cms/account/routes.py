from flask import Blueprint, render_template, request, Response, Flask, jsonify, session, g, redirect
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL
from ..system.config import SystemConfig

# App
app = Flask(__name__)

# Encrypt
bcrypt = Bcrypt(app)

# MySQL
mysql = MySQL()
mysql.init_app(app)
mysql = MySQL(app)

# Blueprint
mod = Blueprint('account', __name__, template_folder='templates')


@mod.route('/')
@mod.route('/me')
def index():
    config = SystemConfig.load_configs()
    if 'user_id' in session:
        # MySQL cursor
        db = mysql.connection.cursor()
        db.execute(f"SELECT id, username, mail, look, rank_class FROM users WHERE id = '{session['user_id']}'")
        result = db.fetchone()
        g.user = result

    return render_template('me.html', config = config)

