class Config:

    # ---- Trabajar de manera Local ----
    SERVER_NAME = "localhost:5000"     # Esto es el nombre del servidor, para trabajar de manera LOCAL
    DEBUG = True
    DB_HOST = "localhost"
    DB_NAME = "DB_PostVenta"
    DB_USER = "postgres"
    DB_PASS = "root"
    DB_PORT = "5432"

    TEMPLATE_FOLDER = "views/templates"      # defino las rutas para los archivos de vista 
    STATIC_FOLDER ="views/static"    