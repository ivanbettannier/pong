import os

# Récupérer le chemin du répertoire du script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Définir le nom du sous-répertoire
subdirectory_name = "assets"

# Chemin complet du sous-répertoire
subdirectory_path = os.path.join(script_directory, subdirectory_name)

# Vérifier si le sous-répertoire existe déjà, sinon le créer
if not os.path.exists(subdirectory_path):
    os.makedirs(subdirectory_path)
    print(f"Le sous-répertoire '{subdirectory_name}' a été créé avec succès.")
else:
    print(f"Le sous-répertoire '{subdirectory_name}' existe déjà.")