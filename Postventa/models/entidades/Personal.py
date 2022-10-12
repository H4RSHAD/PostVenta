from flask_login import UserMixin

class Personal(UserMixin):
    def __init__(self, CI, Nombre, ApellidoP, ApellidoM, Telefono, Correo, Fecha_Nacimiento) ->None:
        self.ci = CI
        self.nombre = Nombre
        self.apellido_paterno = ApellidoP
        self.apellido_materno = ApellidoM
        self.telefono = Telefono
        self.correo = Correo
        self.fecha_nacimiento = Fecha_Nacimiento
        