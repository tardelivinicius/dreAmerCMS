import re
from flask import Blueprint, render_template, request, Response, Flask, jsonify
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL

# App
app = Flask(__name__)

# Encrypt
bcrypt = Bcrypt(app)

# MySQL
mysql = MySQL()
mysql.init_app(app)
mysql = MySQL(app)

# Blueprint
mod = Blueprint('register', __name__, template_folder='templates')

@mod.route('/')
def index():
    # Calcula o ano
    year = 2020 - 12
    year_list = []
    count = 0
    for i in range(year):
        if count == 81:
            break
        year_list.append(year - count)
        count += 1


    if request.method == 'GET':
        if request.args.get('step'):
            if int(request.args.get('step')) == 2:
                return render_template('register2.html', year = year_list, days = [i for i in range(1, 32)])
            if int(request.args.get('step')) == 3:
                return render_template('register3.html')
        else:
            return render_template('register.html')

    return render_template('register.html')

@mod.route('/step1', methods=['POST'])
def register_step1():
    # E-mail Regex
    # EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    data = {}

    # Validation method
    if request.method == 'POST':
        # E-mail Validation
        if request.form['register-mail'] is None:
        # if not EMAIL_REGEX(request.form['register-mail']):
            raise ValueError("O endereço de e-mail deve ser válido")
        else:
            # CONSULTAR O E-MAIL NO BANCO PARA VER SE JÁ EXISTE, GARANTIR QUE NÃO VAI TER E-MAIL DUPLICADO
            data.update({'register-mail': request.form['register-mail']})

        # Nickname Validation
        if request.form['register-username'] is None:
            raise ValueError("É necessário preencher o campo usuário")
        else:
            data.update({'register-username': request.form['register-username'] })

        # Password Validation
        if request.form['register-password'] is None or request.form['register-password-confirm'] is None:
            raise ValueError("É necessário preencher os campos de senha")
        else:
            if request.form['register-password'] == request.form['register-password-confirm']:
                pw_hash = bcrypt.generate_password_hash(request.form['register-password']).decode('utf-8')
                data.update({'register-password': pw_hash})
            else:
                raise ValueError("As senhas não combinam")

        return jsonify(data)

@mod.route('/step2', methods=['POST'])
def register_step2():
    if request.method == 'POST':
        data = {}
        if request.form['gender'] is None:
            raise ValueError("É necessário preencher um gênero")
        else:
            data.update({'gender': request.form['gender']})

        birthday = '{0}-{1}-{2}'.format(request.form['year'], request.form['month'], request.form['day'])
        data.update({'birthday': birthday})

        return jsonify(data)

@mod.route('/step3', methods=['POST'])
def register_step3():

    # Cursor
    cursor = mysql.connection.cursor()

    # Repeat Validation
    if request.method == 'POST':

        print(request.form)
        # E-mail Validation
        if request.form['register-mail'] is None:
        # if not EMAIL_REGEX(request.form['register-mail']):
            raise ValueError("O endereço de e-mail deve ser válido")
        else:
            cursor.execute(f"SELECT * FROM users WHERE mail = '{request.form['register-mail']}' ")
            query = cursor.fetchall()
            if query:
                raise ValueError("O endereço de e-mail já existe")
            else:
                email = request.form['register-mail']

        # Nickname Validation
        if request.form['register-username'] is None:
            raise ValueError("É necessário preencher o campo usuário")
        else:
            username = request.form['register-username']

        # Password Validation
        if request.form['register-password'] is None:
            raise ValueError("É necessário preencher os campos de senha")
        else:
            password = request.form['register-password']

        # Gender Validation
        if request.form['gender'] is None:
            raise ValueError("É necessário preencher um gênero")
        else:
            gender = request.form['gender']

        # Birthday Validation
        # birthday = '{0}-{1}-{2}'.format(request.form['year'], request.form['month'], request.form['day'])

        motto = 'Olá, sou um novo Habbelix!'

        # Avatar Code Validation
        if request.form['avatar_code'] is None:
            raise ValueError("É necessário preencher o avatar")
        else:
            avatar_code = request.form['avatar_code']

        cursor.execute(f'''INSERT INTO users (username, password, mail, auth_ticket, rank_vip, credits, vip_points, activity_points, look, gender, motto, account_created, ip_last, ip_reg)
                       VALUES ('{username}', '{password}', '{email}', 0, 3, 999999, 0, 0, '{avatar_code}', '{gender}', '{motto}', '2020-02-12', '192.168.0.1', '192.168.0.1')''')