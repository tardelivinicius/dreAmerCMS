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
register = Blueprint('register', __name__, template_folder='templates')

@register.route('/')
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
        else:
            return render_template('register.html')

    return render_template('register.html')

@register.route('/step1', methods=['POST'])
def register_step1():
    ''' Validação dos dados básicos '''
    # E-mail Regex
    EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    data = {}

    # Validation method
    if request.method == 'POST':
        # E-mail Validation
        if request.form['register-email'] is None:
        # if not EMAIL_REGEX(request.form['register-email']):
            raise ValueError("O endereço de e-mail deve ser válido")
        else:
            data.update({'register-email': request.form['register-email']})

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

        # Gender Validation
        if request.form['gender'] is None:
            raise ValueError("É necessário preencher um gênero")
        else:
            data.update({'gender': request.form['gender']})

        print(data)
        return jsonify(data)

@register.route('/step2', methods=['POST'])
def register_step2():
    ''' Nova validação e cadastro do usuário '''

    # MySQL cursor
    db = mysql.connection.cursor()

    # Repeat Validation
    if request.method == 'POST':
        # E-mail Validation
        if request.form['register-email'] is None:
        # if not EMAIL_REGEX(request.form['register-email']):
            raise ValueError("O endereço de e-mail deve ser válido")
        else:
            db.execute(f"SELECT * FROM users WHERE mail = '{request.form['register-email']}' ")
            query = db.fetchall()
            if query:
                raise ValueError("O endereço de e-mail já existe")
            else:
                email = request.form['register-email']

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

        motto = 'Olá, sou um novo Habbelix!'

        # Avatar Code Validation
        if request.form['avatar_code'] is None:
            raise ValueError("É necessário preencher o avatar")
        else:
            avatar_code = request.form['avatar_code']

        query = f"""INSERT INTO users (username, password, auth_ticket, vip_points, credits, activity_points, look, gender, motto, mail, account_created, ip_last, ip_reg)
                       VALUES ('{username}', '{password}', 0, 0, 999999, 0, '{avatar_code}', '{gender}', '{motto}', '{email}', NOW(), '192.168.0.1', '192.168.0.1')"""
        db.execute(query)
        mysql.connection.commit()

        db.close()

        return Response('', 200)

@register.route('/check-username-email-exists', methods=['POST'])
def check_username_email_exists():
    # MySQL cursor
    db = mysql.connection.cursor()

    ''' Verifica se existe um e-mail cadastrado '''
    if request.form.get('register-email', None):
        db.execute(f"SELECT * FROM users WHERE mail = '{request.form['register-email']}' ")
        query = db.fetchall()
        if query:
            return Response('E-mail já cadastrado em nosso sistema', 409)

    ''' Verifica se existe um nickname cadastrado '''
    if request.form.get('register-username', None):
        db.execute(f"SELECT * FROM users WHERE username = '{request.form['register-username']}' ")
        query = db.fetchall()
        if query:
            return Response('Nome de usuário já cadastrado em nosso sistema', 409)

    return Response('', 200)
