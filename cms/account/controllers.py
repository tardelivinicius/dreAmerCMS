from flask import Blueprint, render_template, request, Response, Flask, jsonify, session, g, redirect, url_for
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
account = Blueprint('account', __name__, template_folder='templates')

@account.before_request
def before_request():
    if 'user_id' in session:
        # MySQL cursor
        db = mysql.connection.cursor()
        db.execute(f"SELECT id, username, mail, look, `rank`, motto, last_online, account_created FROM users WHERE id = '{session['user_id']}'")
        result = db.fetchone()
        g.user = result

@account.route('/')
@account.route('/me', methods=['POST', 'GET'])
def index():
    config = SystemConfig.load_configs()
    return render_template('me.html', config = config)

@account.route('/profile', methods=['POST', 'GET'])
def profile():
    config = SystemConfig.load_configs()

    if request.method == 'GET':
        db = mysql.connection.cursor()
        if request.args.get('username'):
            query = f"""SELECT U.username FROM Users U WHERE U.username = '{request.args.get('username')}'"""
            db.execute(query)
            result = db.fetchone()
        else:
            query = f"""SELECT U.username FROM Users U WHERE U.id = {session['user_id']}"""
            db.execute(query)
            result = db.fetchone()

        if result:
            # Profile - Basic Data
            query = f"""SELECT U.username, U.motto, U.last_online, U.account_created, U.look FROM Users U WHERE U.username = '{result['username']}'"""
            db.execute(query)
            user = db.fetchone()
            # Profile - Rooms
            query = f"""SELECT R.* FROM rooms R JOIN users U ON U.id = R.owner_name WHERE U.username = '{result['username']}'"""
            db.execute(query)
            user_rooms = db.fetchall()
            # Profile - User Groups
            query = f"""SELECT G.name, G.badge FROM guilds_members GM JOIN `guilds` G ON G.id = GM.guild_id JOIN users U ON U.id = GM.user_id WHERE U.username = '{result['username']}'"""
            db.execute(query)
            user_groups = db.fetchall()
            # Profile - Friends
            query = f"""SELECT U2.username AS username, U2.look AS look FROM messenger_friendships MF JOIN users U ON U.id = MF.user_one_id JOIN users U2 ON U2.id = MF.user_two_id WHERE U.username = '{result['username']}'"""
            db.execute(query)
            user_friends = db.fetchall()

            return render_template('profile.html', config = config, user = user, user_rooms = user_rooms, user_groups = user_groups, user_friends = user_friends)
        else:
            return redirect('me')



@account.route('/settings', methods=['POST', 'GET'])
def setttings():
    config = SystemConfig.load_configs()
    if request.method == 'GET':
        if request.args.get('step') == 'email':
            return render_template('settings/settings_mail.html', config = config)
        elif request.args.get('step') == 'password':
            return render_template('settings/settings_password.html', config = config)
        else:
            return render_template('settings/settings_general.html', config = config)

    return render_template('settings/settings_general.html', config = config)

@account.route('/change_motto', methods=['POST'])
def change_motto():
    if request.method == 'POST':
        db = mysql.connection.cursor()
        query = f""" UPDATE users SET motto = '{request.form['motto']}' WHERE id = {session['user_id']}"""
        db.execute(query)
        mysql.connection.commit()
        db.close()
        return Response('', 202)

@account.route('/save_settings', methods=['POST'])
def save_settings():
    if request.method == 'POST':
        db = mysql.connection.cursor()
        query = f"""UPDATE users SET block_newfriends = '{request.form['block_new_friends']}', hide_inroom = '{request.form['hide_in_room']}', hide_online = '{request.form['hide_online']}' WHERE id = {session['user_id']}"""
        db.execute(query)
        mysql.connection.commit()
        db.close()
        return Response('', 200)

@account.route('/save_settings_mail', methods=['POST'])
def save_settings_mail():
    if request.method == 'POST':
        db = mysql.connection.cursor()
        if request.form['old_email'] is not None:
            query = f"""SELECT mail FROM users WHERE id = {session['user_id']} AND mail = '{request.form['old_email']}' """
            db.execute(query)
            result = db.fetchone()
            if not result:
                return Response({"E-mail informado não pertence ao usuário"}, 409)
        else:
            return Response({"É necessário preencher o e-mail atual"}, 409)

        if request.form['new_email'] is None:
            return Response({"É necessário preencher um e-mail novo"}, 409)

        if request.form['password_confirm'] is None:
            return Response({"É necessário preencher a senha para confirmar a operação"}, 409)

        # Check User
        query = f"""SELECT id, mail, password FROM users WHERE id = {session['user_id']} AND mail = '{request.form['old_email']}' """
        db.execute(query)
        check_user = db.fetchone()

        if check_user:
            # Check if new email is available
            query = f"""SELECT mail FROM users WHERE mail = '{request.form['new_email']}' """
            db.execute(query)
            check_new_email_existance = db.fetchone()
            # If available
            if not check_new_email_existance:
                # Password Validation
                if bcrypt.check_password_hash(check_user['password'], str(request.form['password_confirm'])):
                    query = f"""UPDATE users SET mail = '{request.form['new_email']}' WHERE id = {session['user_id']} AND mail = '{request.form['old_email']}' """
                    db.execute(query)
                    mysql.connection.commit()
                    db.close()
                    return Response('', 200)
                else:
                    return Response({"Senha informada inválida"}, 409)
            else:
                return Response({"E-mail já cadastrado para outro usuário"}, 409)

@account.route('/save_settings_password', methods=['POST'])
def save_settings_password():
    if request.method == 'POST':
        db = mysql.connection.cursor()
        if request.form['email_confirm'] is not None:
            query = f"""SELECT mail FROM users WHERE id = {session['user_id']} AND mail = '{request.form['email_confirm']}' """
            db.execute(query)
            result = db.fetchone()
            if not result:
                return Response({"E-mail informado não pertence ao usuário"}, 409)
        else:
            return Response({"É necessário preencher o e-mail para confirmar a operação"}, 409)

        if request.form['old_password'] is None:
            return Response({"É necessário preencher a senha atual"}, 409)

        if request.form['new_password'] is None:
            return Response({"É necessário preencher uma nova senha"}, 409)

        # Check User
        query = f"""SELECT password FROM users WHERE id = {session['user_id']} AND mail = '{request.form['email_confirm']}' """
        db.execute(query)
        check_user_password = db.fetchone()

        if check_user_password:

            if bcrypt.check_password_hash(check_user_password['password'], str(request.form['old_password'])):
                new_password_hash = bcrypt.generate_password_hash(request.form['new_password']).decode('utf-8')
                query = f"""UPDATE users SET password = '{new_password_hash}' WHERE id = {session['user_id']} AND mail = '{request.form['email_confirm']}' """
                db.execute(query)
                mysql.connection.commit()
                db.close()
                return Response('', 200)
            else:
                return Response({"A senha atual não confere com o banco de dados"}, 409)

        else:
            return Response({"E-mail informado não existe"}, 409)