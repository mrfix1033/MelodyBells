import os

import yaml

from mrfix1033.melodybells.data.File import File


def create_files():
    list_dirs_to_create = ["app/locales"]

    for dir_name in list_dirs_to_create:
        os.makedirs(dir_name, exist_ok=True)

    
