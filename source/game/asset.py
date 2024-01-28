import os

# Get script directory path
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the name of sub-directory
subdirectory_name = "assets"

# Full path of the subdirectory
subdirectory_path = os.path.join(script_directory, subdirectory_name)

# Check if sub-directory already exists, otherwise create it
if not os.path.exists(subdirectory_path):
    os.makedirs(subdirectory_path)
    print(f"Le sous-répertoire '{subdirectory_name}' a été créé avec succès.")
else:
    print(f"Le sous-répertoire '{subdirectory_name}' existe déjà.")