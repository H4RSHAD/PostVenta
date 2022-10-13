from crypt import methods
from pickle import GET
from flask import Blueprint, request
from ..controller import ClienteController
from ..models.entidades import Cliente

cliente_scope = Blueprint('cliente', __name__)

@cliente_scope.route('/index', methods=['GET'])
def get_list():
    pass

@cliente_scope.route('/create', methods=['POST'])
def create():
    data = request.form
    print(data)
    cliente = Cliente(ci=data["ci"], nombre_completo=data["nombre_completo"],
                        telefono=data["telefono"], nit=data["nit"], estado=data["estado"])

    pass

@cliente_scope.route('/update/<ci_>', methods=['PUT'])
def update(ci_):
    pass

@cliente_scope.route('/delete/<ci_>', methods=['DELETE'])
def delete(ci_):
    pass

