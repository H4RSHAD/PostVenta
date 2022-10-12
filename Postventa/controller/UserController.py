from ..models.entidades.User import User
from ..database import usuario_db

def create(usuario: User)->User:
    return usuario_db.create(usuario)

def update(usuario: User) -> User:
    return usuario_db.update(usuario)


def delete(usuario: User) -> User:
    return usuario_db.delete(usuario)

#Devuelve lista completa 
def list():
    return usuario_db.list_all()        

def login(usuario: User) -> User:
    return usuario_db.login(usuario)