from ..models.entidades.Cliente import Cliente
from ..database import cliente_db

def create(cliente: Cliente)->Cliente:
    return cliente_db.create(cliente)

def update(cliente: Cliente) -> Cliente:
    return cliente_db.update(cliente)


def delete(cliente: Cliente) -> Cliente:
    return cliente_db.delete(cliente)

#Devuelve lista completa 
def list():
    return cliente_db.list_all()        

