from contextlib import contextmanager
import psycopg2
from config import Config

@contextmanager
def __get_cursor():
    conexion_db = psycopg2.connect(host =Config.DB_HOST, database= Config.DB_NAME, user = Config.DB_USER, password = Config.DB_PASS, port = Config.DB_PORT )
    cursor = conexion_db.cursor()

    try:
        yield cursor
        conexion_db.commit()
        print('Conexion con la base de datos " Exitosa desde conection"')
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
        conexion_db.close()
        print("Conexion finalizada")
    print(conexion_db)




def _fetch_one(consulta, parametros):      # devolvera el primero
    if parametros is None:
        parametros = []

    with __get_cursor() as cursor:         # hacemos la conexion 
        cursor.execute(consulta,parametros) # hacemos la consulta
        return cursor.fetchone()            # devolvemos el resultado en una tupla
    


def _fetch_all(consulta,parametros):       #dolvera todo
    if parametros is None:
        parametros = []

    with __get_cursor() as cursor:
        cursor.execute(consulta,parametros)
        return cursor.fetchall()


def _fetch_none(consulta,parametros):     #no devuelve
    if parametros is None:
        parametros = []

    with __get_cursor() as cursor:
        cursor.execute(consulta,parametros)


def _fecth_lastrow_id(consulta,parametros):
    if parametros is None:
        parametros = []

    with __get_cursor() as cursor:
        cursor.execute(consulta,parametros)
        return cursor.lastrowid()