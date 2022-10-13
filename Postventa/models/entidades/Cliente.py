from flask_login import UserMixin

class Cliente(UserMixin):
    def __init__(self, CI, Nombre_completo, Telefono, NIT, estado)->None:
        self.ci = CI
        self.nombre_completo = Nombre_completo
        self.telefono = Telefono
        self.nit = NIT
        self.estado = estado

