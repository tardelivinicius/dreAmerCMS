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
system_login = Blueprint('login', __name__, template_folder='templates')

@system_login.route('/')
def index():
    config = SystemConfig.load_configs()
    if 'user_id' in session:
        return redirect('/account/me')

    return render_template('index.html', config = config)

@system_login.before_request
def before_request():
    config = SystemConfig.load_configs()
    if 'user_id' in session:
        # MySQL cursor
        db = mysql.connection.cursor()
        db.execute(f"SELECT id, username, mail FROM users WHERE id = '{session['user_id']}'")
        result = db.fetchone()
        g.user = result

@system_login.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)
        # MySQL cursor
        db = mysql.connection.cursor()
        if request.form['username'] is not None and request.form['password'] is not None:
            db.execute(f"SELECT id, username, mail, password, `rank` FROM users WHERE username = '{request.form['username']}' OR mail = '{request.form['username']}'")
            result = db.fetchone()
            # Verify Result
            if result:
                # Password Encrypt Validate
                if bcrypt.check_password_hash(result['password'], str(request.form['password'])):
                    # User is LOGGED, mount session()
                    session['user_id'] = result['id']
                    session['rank'] = result['rank']
                    # TODO - CRIAR UMA TABELA PARA ISSO
                    # db.execute(f"INSERT INTO heliocms_sessions (userid, ip, date, browser) VALUES('{result['id']}', '192.168.0.1', '2020-02-12', 'Chrome')")
                    # mysql.connection.commit()
                    # db.close()
                    return Response('', 201)
                else:
                    return Response('', 404)

            else:
                print('Usuário ou senha inválidos')
                return Response('Usuário ou senha inválidos', 404)

@system_login.route('/logout')
def logout():
    session.clear()
    return redirect('/')
