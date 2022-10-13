from flask_login import UserMixin

class Personal(UserMixin):
    def __init__(self,ID, Nombre, ApellidoP, ApellidoM, Telefono, CI, Correo, Fecha_Nacimiento, ID_usuario) ->None:
        self.id = ID
        self.nombre = Nombre
        self.apellido_paterno = ApellidoP
        self.apellido_materno = ApellidoM
        self.telefono = Telefono
        self.ci = CI
        self.correo = Correo
        self.fecha_nacimiento = Fecha_Nacimiento
        self.id_usuario = ID_usuario
        