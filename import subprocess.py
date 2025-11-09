import subprocess
import os
from datetime import datetime

# Configuración de la base de datos
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = " "
DB_NAME = "api_vue"

# Ruta donde se guardará el backup
BACKUP_DIR = "C:\Users\josss\Desktop\Back ups"
os.makedirs(BACKUP_DIR, exist_ok=True)  # Crear directorio si no existe

# Nombre del archivo de backup
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_file = os.path.join(BACKUP_DIR, f"{DB_NAME}_backup_{timestamp}.sql")

# Comando para ejecutar mysqldump
dump_command = [
    "mysqldump",
    f"-h{DB_HOST}",
    f"-u{DB_USER}",
    f"-p{DB_PASSWORD}",
    DB_NAME,
]

try:
    # Abrir archivo y redirigir la salida del comando mysqldump
    with open(backup_file, "w") as f:
        subprocess.run(dump_command, stdout=f, check=True)
    print(f"Backup completado: {backup_file}")
except subprocess.CalledProcessError as e:
    print(f"Error al realizar el backup: {e}")
