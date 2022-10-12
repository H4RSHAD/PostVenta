from flask import session
from ..models.entidades.User import User
from .connection import _fecth_lastrow_id,_fetch_one,_fetch_none,_fetch_all

def create(usuario: User)->User: 
    sql = """ INSERT INTO Usuario VALUES({},'{}','{}','{}','{}')
          """.format(usuario.id, usuario.username, usuario.password, usuario.id_rol, usuario.id_persona)

    _fetch_none(sql,None)
    return usuario


def update(usuario: User)->User: 
    pass

def delete(usuario: User)->User: 
    pass

def list_all(usuario: User)->User: 
    pass

def login(usuario: User)->User: 
    sql = """ SELECT ID, Nombre, Contraseña, ID_Rol, ID_persona FROM Usuario WHERE
          Nombre = '{}' """.format(usuario.username)
    
    row = _fetch_one(sql,None)
    if row !=None:
        usuario = User(row[0],row[1], (User.check_password(row[2],(usuario.password))), row[3],row[4])
        print(usuario.username)
        return usuario  # El usuario se encuentra en la BD_Lab
    else:
        return None # no hay usuario