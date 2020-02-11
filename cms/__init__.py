from flask import Flask

app = Flask(__name__)

from cms.login.routes import mod
from cms.register.routes import mod

app.register_blueprint(login.routes.mod)
app.register_blueprint(register.routes.mod, url_prefix='/register')