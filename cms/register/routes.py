import re
from flask import Blueprint, render_template, request, Response, Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

mod = Blueprint('register', __name__, template_folder='templates')


@mod.route('/')
def index():
    year = 2020 - 12
    year_list = []
    count = 0
    for i in range(year):
        if count == 81:
            break
        year_list.append(year - count)
        count += 1

    return render_template('register.html')

@mod.route('/step1', methods=['POST'])
def register_step1():
    # E-mail Regex
    # EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    data = {}

    print(request.form)
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
                print(pw_hash)
                data.update({'register-password': pw_hash})
            else:
                raise ValueError("As senhas não combinam")

        print(data)
        return Response(data, status=200, mimetype='application/json')