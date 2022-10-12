from flask_login import UserMixin

class Rol(UserMixin):
    def __init__(self, ID, Descripcion):
        self.id = ID
        self.descricion = Descripcion
