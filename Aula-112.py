import os # tratar pastas
import shutil # ações em lotes

from_dir = "c://Users//comma//Downloads"
to_dir = "c://Users//comma//OneDrive//Área de Trabalho//Imagens"
list_of_files = os.listdir(from_dir)

print(list_of_files) 

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    print(name, extension)