import pytest
import os
from cifpy.utils.folder import get_file_count, get_file_path_list


@pytest.fixture
def cif_directory():
    return "tests/data/cif/folder"


def test_get_file_count(cif_directory):
    count = get_file_count(cif_directory, ext=".cif")
    assert count == 3


def test_get_file_path_list(cif_directory):
    expected_files = {"300169.cif", "300170.cif", "300171.cif"}
    file_paths = get_file_path_list(cif_directory, ext=".cif")
    found_files = {os.path.basename(path) for path in file_paths}
    assert expected_files == found_files
    assert len(file_paths) == 3
