import os
from os.path import join, exists
import glob
from shutil import rmtree, move


def get_file_count(directory, ext=".cif"):
    """Counts files with a given extension in a directory."""
    return len(glob.glob(os.path.join(directory, f"*{ext}")))


def get_file_path_list(directory, ext=".cif"):
    """Returns a list of file paths with a given extension from a directory."""
    return glob.glob(os.path.join(directory, f"*{ext}"))
