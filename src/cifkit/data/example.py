import os
from enum import Enum


class Example(str, Enum):
    def get_path(*args):
        return os.path.join(os.path.dirname(__file__), *args)

    ErCoIn_folder_path = get_path("ErCoIn")
    ErCoIn_big_folder_path = get_path("ErCoIn_big")
    Er10Co9In20_file_path = get_path("ErCoIn", "Er10Co9In20.cif")
    ErCo2_68In0_32_file_path = get_path("ErCoIn", "ErCo2.68In0.32.cif")
    ErCoIn5_file_path = get_path("ErCoIn", "ErCoIn5.cif")
