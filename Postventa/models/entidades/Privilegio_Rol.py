from flask_login import UserMixin

class Rol(UserMixin):
    def __init__(self, ID_Privilegio, ID_Rol):
        self.id_privilegio = ID_Privilegio
        self.id_rol = ID_Rol
