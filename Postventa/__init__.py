from flask import Flask
from config import Config
from flask_wtf.csrf import CSRFProtect

#Rutas
from .router import tipo_login


csrf = CSRFProtect() # instancia de proteccion

Postventa = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER )
Postventa.config.from_object(Config)
csrf.init_app(Postventa)



#llamadas a las rutas
Postventa.register_blueprint(tipo_login, url_prefix = "/")