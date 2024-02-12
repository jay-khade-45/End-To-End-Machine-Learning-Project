import os
from pathlib import Path
import logging

# creating log format
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# project name dir -> where actual code resides
project_name = "mlproject"

# project structure.
# list of dirs and files we need to create.
list_of_files = [
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
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

# creating the above-mentioned folder structure
for filepath in list_of_files:

    filepath = Path(filepath)
    file_dir, file_name = os.path.split(filepath)
    # print(f"file_dir={file_dir}, file_name={file_name}")
    # print()
    # print("*"*50)
    # print()

    # if folder creation is required
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating DIR; {file_dir} for the file: {file_name}")

    # now the folder is created -> we can create the file
    # if file does not exist and or if it exists and have a size of 0.
    # we can create a file.

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # create file
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty file: {filepath}")

    else:
        # file already exists
        logging.info(f"{file_name} is already exist")
