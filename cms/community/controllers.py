from flask import Blueprint, render_template, request, Response, Flask, jsonify, session, g, redirect
from flask_mysqldb import MySQL
from ..system.config import SystemConfig

# App
app = Flask(__name__)

# MySQL
mysql = MySQL()
mysql.init_app(app)
mysql = MySQL(app)

# Blueprint
community = Blueprint('community', __name__, template_folder='templates')


@community.before_request
def before_request():
    if 'user_id' in session:
        # MySQL cursor
        db = mysql.connection.cursor()
        db.execute(f"SELECT id, username, mail, look, `rank`, motto, last_online, account_created FROM users WHERE id = '{session['user_id']}'")
        result = db.fetchone()
        g.user = result


@community.route('/news', methods=['POST', 'GET'])
def news():
    config = SystemConfig.load_configs()
    return render_template('news.html', config = config)

@community.route('/staffs', methods=['POST', 'GET'])
def staffs():
    config = SystemConfig.load_configs()

    db = mysql.connection.cursor()

    # Staff - CEO
    query = f"""SELECT U.username, U.motto, U.look, U.online FROM Users U JOIN ranks R ON R.id = U.`rank` WHERE U.`rank` = 9"""
    db.execute(query)
    ceo_users = db.fetchall()
    # Staff - Administração
    query = f"""SELECT U.username, U.motto, U.look, U.online FROM Users U JOIN ranks R ON R.id = U.`rank` WHERE U.`rank` = 8"""
    db.execute(query)
    admin_users = db.fetchall()
    # Staff - Moderação
    query = f"""SELECT U.username, U.motto, U.look, U.online FROM Users U JOIN ranks R ON R.id = U.`rank` WHERE U.`rank` = 7"""
    db.execute(query)
    mod_users = db.fetchall()

    return render_template('staffs.html', config = config, ceo_users = ceo_users, admin_users = admin_users, mod_users = mod_users)
