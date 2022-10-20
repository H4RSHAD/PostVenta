from flask import Blueprint, request, session, render_template
from ..controller import UserController
from ..models.entidades import Cliente

cliente_scope = Blueprint('cliente',__name__)

@cliente_scope.route('/', methods=['GET'])
def get_list():
        #return ('<h1>Entro el cliente</h1>')
    if 'Esta_logeado' in session:
                # Aqui ponemos Titulo y descripcion 
        parametros = { "title": "Restaurant virtual",
                        "description": "Bienvenido(a) ",
                        "Nombre":'CAJERO',
                        "tipo": "Administrador"
        }
        
        return render_template("usuario/cajero/dashboard_cajero.html",**parametros)

@cliente_scope.route('/create', methods=['POST'])
def create():
    '''
    data = request.form
    print(data)
    cliente = Cliente(ci=data["ci"], nombre_completo=data["nombre_completo"],
                        telefono=data["telefono"], nit=data["nit"], estado=data["estado"])
    '''
    return ('<h1>Entro el crear cliente</h1>')
    

@cliente_scope.route('/update/<ci_>', methods=['PUT'])
def update(ci_):
    pass

@cliente_scope.route('/delete/<ci_>', methods=['DELETE'])
def delete(ci_):
    pass

@cliente_scope.route('/show_cliente', methods=['GET'])
def show_cliente():
    parametros = { "title": "Res",
                        "description": "Bienvenido(a) ",
                        "Nombre":'',
                        "tipo": "Administrador",
                        "titulo": "Visualizar Usuarios",
                        "titulo_usuario":"Listados de los Usuarios que interactuan con el Sistema"
                }
    clientes_lista = UserController.list()
    return render_template("cliente/cliente.html", ** parametros, items =  clientes_lista)


    