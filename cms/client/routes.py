import pathlib
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

@mod.route('/')
def client():
    config = SystemConfig.load_configs()
    return render_template('client.html', config = config)

@mod.route('/hh_human_body.swf')
def hh_human_body_swf():
    return send_from_directory('static', filename='swf/gordon/PRODUCTION-201602082203-712976078/hh_human_body.swf')

@mod.route('/hh_human_item.swf')
def hh_human_item():
    return send_from_directory('static', filename='swf/gordon/PRODUCTION-201602082203-712976078/hh_human_item.swf')
