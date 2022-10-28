from flask import Blueprint,request,session,flash,render_template,redirect,url_for

from ..controller import UserController
from ..models.entidades.User import User

tipo_login = Blueprint('login',__name__)

@tipo_login.route('/',methods=['GET','POST'])
def login():

    if request.method == 'POST':
        data = request.form
        print(data['password'])
        usuario = User(0,data['username'],data['password'],0,0)
        logger_user = UserController.login(usuario)

        if logger_user != None:

            if logger_user.password:
                print(logger_user.password)

                session['Esta_logeado'] = True
                session['estado'] = logger_user.estado
                session['id_rol'] = logger_user.id_rol
                #return ('<h1>Entro el login</h1>')
                #return redirect(url_for('login.admin'))
                return redirect(url_for('cliente.get_list'))
            else:
                flash("Usuario o contraseña invalida")
                return render_template('auth/login.html')
        else:
            flash("Usuario o contraseña invalida")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')



#----------------------ADMIN------------------------------
@tipo_login.route('/admin',methods=['GET'])
def admin():
    if 'Esta_logeado' in session:
                # Aqui ponemos Titulo y descripcion 
        parametros = { "title": "Restaurant virtual",
                        "description": "Bienvenido(a) ",
                        "Nombre":'admin',
                        "tipo": "Administrador"
        }
        
        return render_template("usuario/admin/dashboard_admin.html",**parametros)
    return redirect(url_for('login'))


#----------------------ROLES------------------------------
@tipo_login.route('/roles',methods=['GET'])
def roles():
    if 'Esta_logeado' in session:
                # Aqui ponemos Titulo y descripcion 
        parametros = { "title": "Biomec virtual",
                        "description": "Bienvenido(a) ",
                        "Nombre":'',
                        "tipo": "Administrador",
                        "titulo": "Visualizar Usuarios",
                        "titulo_usuario":"Listados de los Usuarios que interactuan con el Sistema"
                }
        return render_template("usuario/tipo.html", **parametros)
    return redirect(url_for('login'))





#----------------------Salida -----------------
@tipo_login.route('/')
def logout():
    if 'Esta_logeado' in session:  
        session.pop('Esta_logeado',None)
        session.pop('username',None)
        print(session)
        return render_template('login/')
    return render_template('login/')
