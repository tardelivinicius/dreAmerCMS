from flask import Blueprint, render_template, request, Response, Flask, jsonify, session, g, redirect
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL
from ..system.config import SystemConfig, PERMISSION_MOD, PERMISSION_ADMIN, PERMISSION_MANAGER, PERMISSION_CEO

# App
app = Flask(__name__)

# Encrypt
bcrypt = Bcrypt(app)

# MySQL
mysql = MySQL()
mysql.init_app(app)
mysql = MySQL(app)

# Blueprint
mod = Blueprint('admin', __name__, template_folder='templates')

@mod.before_request
def before_request():
    if 'user_id' in session:
        # MySQL cursor
        db = mysql.connection.cursor()
        db.execute(f"SELECT id, username, mail, `rank`, look FROM users WHERE id = '{session['user_id']}'")
        result = db.fetchone()
        g.user = result

@mod.route('/')
def index():
    config = SystemConfig.load_configs()
    return render_template('admin.html', config = config)

@mod.route('/client')
def admin_client():
    config = SystemConfig.load_configs()
    return render_template('admin_client.html', config = config)

@mod.route('/client_save', methods=['POST'])
def client_save():
    config = SystemConfig.load_configs()

    print(config['id'])
    if request.method == 'POST':

        connection_info_host = request.form.get('connection.info.host', config['connection.info.host']) 
        connection_info_port = request.form.get('connection.info.port', config['connection.info.port'])
        hotel_url = request.form.get('hotel_url', config['hotel_url'])
        client_starting = request.form.get('client.starting', config['client.starting'])
        flash_client_url = request.form.get('flash.client.url', config['flash.client.url'])
        external_variables_txt = request.form.get('external.variables.txt', config['external.variables.txt'])
        external_override_variables_txt = request.form.get('external.override.variables.txt', config['external.override.variables.txt'])
        external_texts_txt = request.form.get('external.texts.txt', config['external.texts.txt'])
        external_override_texts_txt = request.form.get('external.override.texts.txt', config['external.override.texts.txt'])
        external_figurepartlist_txt = request.form.get('external.figurepartlist.txt', config['external.figurepartlist.txt'])
        flash_dynamic_avatar_download_configuration = request.form.get('flash.dynamic.avatar.download.configuration', config['flash.dynamic.avatar.download.configuration'])
        productdata_load_url = request.form.get('productdata.load.url', config['productdata.load.url'])
        furnidata_load_url = request.form.get('furnidata.load.url', config['furnidata.load.url'])
        processlog_enabled = request.form.get('processlog.enabled', config['processlog.enabled'])
        ads_domain = request.form.get('ads.domain', config['ads.domain'])

        # MySQL cursor
        db = mysql.connection.cursor()

        query = f"""UPDATE cms_settings SET `connection.info.host` = '{connection_info_host}', `connection.info.port` = '{connection_info_port}', `hotel_url` = '{hotel_url}', 
        `client.starting` = '{client_starting}', `flash.client.url` = '{flash_client_url}', `external.variables.txt` = '{external_variables_txt}', 
        `external.override.variables.txt` = '{external_override_variables_txt}', `external.texts.txt` = '{external_texts_txt}', 
        `external.override.texts.txt` = '{external_override_texts_txt}', `external.figurepartlist.txt` = '{external_figurepartlist_txt}', 
        `flash.dynamic.avatar.download.configuration` = '{flash_dynamic_avatar_download_configuration}', `productdata.load.url` = '{productdata_load_url}',
        `furnidata.load.url` = '{furnidata_load_url}', `processlog.enabled` = '{processlog_enabled}', `ads.domain` = '{ads_domain}' WHERE id = {config['id']}"""
        db.execute(query)
        mysql.connection.commit()
        db.close()
        return Response('', 200)
        
@mod.route('/system')
def system():
    config = SystemConfig.load_configs()
    return render_template('system.html', config = config)