from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, ID, Nombre, Contraseña, ID_Rol, Estado ) -> None:
        self.id = ID
        self.username = Nombre
        self.password = generate_password_hash(str(Contraseña))
        self.id_rol = ID_Rol
        self.estado = Estado

        
    @classmethod  # Lo decoro con metodo de clase para poder usar (instanciar) este metodo en otro archivo
    def check_password(self,hashed_password, password):

        return check_password_hash(hashed_password, password)        