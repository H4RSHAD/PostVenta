from flask_login import UserMixin

class Rol(UserMixin):
    def __init__(self, ID, Nombre):
        self.id = ID
        self.nombre = Nombre
