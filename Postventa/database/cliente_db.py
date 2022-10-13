from xmlrpc.client import boolean
from ..models.entidades.Cliente import Cliente
from .connection import _fecth_lastrow_id, _fetch_all, _fetch_none, _fetch_one
from typing import List

def create(cliente: Cliente)->Cliente:
    sql = """" INSERT INTO Cliente VALUES({},'{}','{}','{}')
    """.format(cliente.ci, cliente.nombre_completo, cliente.telefono, cliente.nit)

    _fetch_none(sql,None)
    return cliente

def update(cliente: Cliente)->Cliente:

    sql = """ UPDATE CLIENTE SET nombre_completo = '{}' , telefono = '{}', nit = '{}'  where ci = '{}'
            """ .format(cliente.nombre_completo, cliente.telefono, cliente.nit, cliente.ci)
    
    _fetch_none(sql,None)
    return Cliente

def delete(cliente: Cliente)->Cliente:
    sql = """ UPDATE CLIENTE SET estado = '{}'  where ci = '{}'
            """ .format(cliente.estado, cliente.ci)
    
    _fetch_none(sql,None)
    return Cliente

def list_all()  -> List[Cliente]: #LISTO FUNCIONA
    sql = "SELECT * FROM Cliente ORDER BY CI DESC"
    #print(sql) 
    cliente_lista_sql = _fetch_all(sql,None)
    print(cliente_lista_sql[0][1])

    clientes_lista = list(cliente_lista_sql)
    cliente_lista = [] #Tupla que devolvera todos los datos de la tabla Cliente

    for x in range(len(clientes_lista)):
        #Almaceno los respecitvos atributos de la tabla
        ci = clientes_lista[x][0]
        nombre_completo = clientes_lista[x][1]
        telefono = clientes_lista[x][2]
        nit = clientes_lista[x][3]
        estado = clientes_lista[x][4]
        # Creo un diccionario con su respectivo encabezado y asigno el atributo correspondiente
        cliente_datos = { 'ci':ci, 'nombre_completo':nombre_completo,'telefono':telefono,'nit':nit,'estado':estado}
        # por cada interaccion lo guardo el diccionario de los datos de cada cliente en la lista
        cliente_lista.append(cliente_datos)

    return cliente_lista

#verifica si existe el cliente, devuelve boolean
def exit_cliente(atributo: str, value: str) -> bool:
    sql = """ SELECT CI, Nombre_completo, Telefono, nit, estado FROM Cliente WHERE {}  = '{}' """ .format(atributo,value) #la variable del modelo cliente
    existe = _fetch_one(sql,None)

    return existe

# obtiene todos los datos de un cliente
def obtener_cliente(atributo: int)->Cliente:
    sql = """ SELECT * FROM CLIENTE WHERE CI = '{}' """ .format(atributo)

    return sql
