import random
from flask import Blueprint, render_template, request, Response, Flask, jsonify, session, g, redirect, send_from_directory, url_for
from flask_mysqldb import MySQL
from ..system.config import SystemConfig

# App
app = Flask(__name__)

# MySQL
mysql = MySQL()
mysql.init_app(app)
mysql = MySQL(app)

# Blueprint
mod = Blueprint('client', __name__, template_folder='templates')


@mod.before_request
def before_request():
    if 'user_id' in session:
        # MySQL cursor
        db = mysql.connection.cursor()
        # Generate Auth Token
        auth_ticket = '{0}{1}'.format('HabbelixCMS-', random.getrandbits(32))
        # Update User Auth
        db.execute(f"UPDATE users SET auth_ticket = '{auth_ticket}' WHERE id = '{session['user_id']}'")
        mysql.connection.commit()
        # Fetch User
        db.execute(f"SELECT id, auth_ticket FROM users WHERE id = '{session['user_id']}'")
        result = db.fetchone()
        g.user = result


@mod.route('/')
def client():
    config = SystemConfig.load_configs()
    return render_template('client.html', config = config)

@mod.route('/hh_human_item.swf')
def hh_human_body_swf():
    return send_from_directory('static', filename='swf/gordon/PRODUCTION-201601012205-226667486/hh_human_body.swf')

@mod.route('/hh_human_item.swf')
def hh_human_item():
    return send_from_directory('static', filename='swf/gordon/PRODUCTION-201601012205-226667486/hh_human_item.swf')
