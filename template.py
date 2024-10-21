import os 
from pathlib import Path

# Importation du module logging pour gérer l'affichage des messages de journalisation (logs)
import logging

# Configuration de base du module logging :
# - 'level=logging.INFO' signifie que seuls les messages de niveau INFO ou supérieur seront affichés.
# - 'format' permet de personnaliser l'affichage des messages de log avec un horodatage (date et heure) suivi du message.
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "mlProject"


list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"


]
for filepath in list_of_files:
    # Convertir le chemin du fichier en un objet Path pour une manipulation facile des chemins
    filepath = Path(filepath)
    # Séparer le chemin du fichier (filedir) et le nom du fichier (filename)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        # Créer le répertoire s'il n'existe pas déjà (exist_ok=True évite une erreur si le répertoire existe déjà)
        os.makedirs(filedir, exist_ok=True)
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            # Enregistrer un message dans les logs pour indiquer la création du fichier vide

            logging.info(f"Creating empty file: {filepath}")

     # Enregistrer un message dans les logs pour indiquer que le fichier existe déjà
    else:
        logging.info(f"{filename} is already exists")