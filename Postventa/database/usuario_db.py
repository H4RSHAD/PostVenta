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

def list_all(): 
    sql = "SELECT * FROM Usuario"
    print(sql) 
    usuario_lista_sql = _fetch_all(sql,None)

    usuarios_lista = list(usuario_lista_sql)
    usuario_lista = [] #Tupla que devolvera todos los datos de la tabla Usuario
    #id_roles =['','Admin','Cajero','Mesero'] #lista de roles, el primero es vacio porque es 0
    for x in range(len(usuarios_lista)):
        id_user = usuarios_lista[x][0]
        nombre = usuarios_lista[x][1]
        contraseña = str(usuarios_lista[x][2])
        id_rol = usuarios_lista[x][3]
        id_estado = usuarios_lista[x][4]
        #Este es un ciclo para poder mostrar en string su tipo de rol y no mostrar numero
        '''
        for i in range(len(id_roles)):
            if i == id_rol:
                id_rol = id_roles[i]
        id_persona= usuarios_lista[x][4]
        '''
        # Creo un diccionario con su respectivo encabezado y asigno el atributo correspondiente
        print(contraseña)
        usuario_datos = { 'id':id_user, 'nombre':nombre,'contraseña':contraseña,'id_rol':id_rol,'estado':id_estado}
        # por cada interaccion lo guardo el diccionario de los datos de cada persona en la lista
        usuario_lista.append(usuario_datos)

    return usuario_lista


def login(usuario: User)->User: 
    sql = """ SELECT ID, Nombre, Contraseña, ID_Rol, Estado FROM Usuario WHERE
          Nombre = '{}' """.format(usuario.username)
    
    row = _fetch_one(sql,None)
    if row !=None:
        usuario = User(row[0],row[1], (User.check_password(row[2],(usuario.password))), row[3],row[4])
        print(usuario.estado)
        return usuario  # El usuario se encuentra en la BD_Lab
    else:
        return None # no hay usuario