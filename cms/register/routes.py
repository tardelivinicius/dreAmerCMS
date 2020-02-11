from flask import Blueprint, render_template, request

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

@mod.route('/save', methods=['POST'])
def save():
    print('email', request.form['email'])
    print('oi, vou salvar as informações')