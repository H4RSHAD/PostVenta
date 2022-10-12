from flask import Blueprint,request,session,flash,render_template

from ..controller import UserController
from ..models.entidades.User import User

tipo_login = Blueprint('login',__name__)

@tipo_login.route('/',methods=['GET','POST'])
def login():

    if request.method == 'POST':
        data = request.form

        usuario = User(0,data['username'],data['password'],0,0)

        logger_user = UserController.login(usuario)

        if logger_user != None:

            if logger_user.password:

                session['Esta_logeado'] = True
                session['id_persona'] = logger_user.id_persona
                session['id_rol'] = logger_user.id_rol

            else:
                flash("Usuario o contraseña invalida")
                return render_template('auth/login.html')
        else:
            flash("Usuario o contraseña invalida")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')
