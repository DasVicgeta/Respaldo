import os
from git import Repo
from datetime import datetime

# --- CONFIGURACIÓN ---
PATH_REPOSITORIO_LOCAL = 'ruta/a/tu/carpeta/local'
MENSAJE_COMMIT = f"Backup automático - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
NOMBRE_RAMA = 'main'  # o 'master'

def hacer_backup():
    try:
        # Abrir el repositorio existente
        repo = Repo(PATH_REPOSITORIO_LOCAL)
        
        if not repo.bare:
            print(f"Verificando cambios en: {PATH_REPOSITORIO_LOCAL}")
            
            # 1. Añadir todos los archivos nuevos/modificados
            repo.git.add(A=True)
            
            # 2. Verificar si hay algo nuevo para commitear
            if repo.is_dirty(untracked_files=True):
                # 3. Hacer el commit
                repo.index.commit(MENSAJE_COMMIT)
                print(f"Commit realizado: {MENSAJE_COMMIT}")
                
                # 4. Hacer el Push
                origin = repo.remote(name='origin')
                origin.push(NOMBRE_RAMA)
                print("¡Backup subido a GitHub con éxito!")
            else:
                print("No hay cambios detectados para respaldar.")
        else:
            print("Error: No se encontró un repositorio válido en esa ruta.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    hacer_backup()