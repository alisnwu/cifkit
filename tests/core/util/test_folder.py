import pytest
import os
from cifpy.utils.folder import (
    get_file_path,
    get_file_count,
    get_file_path_list,
    make_output_folder,
    check_file_exists,
    check_file_not_empty,
)

from cifpy.utils.error_messages import FileError


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


def test_make_output_folder(tmp_path: str):
    new_folder_name = "plot"
    dir_path = tmp_path

    # Path where the new folder should be created
    expected_path = tmp_path / new_folder_name
    make_output_folder(dir_path, new_folder_name)

    # Check if the folder was created correctly
    assert os.path.exists(expected_path)
    assert expected_path.is_dir()


def test_get_file_path(tmp_path: str):
    dir_path = tmp_path
    file_name = "example.py"
    # Expected path combining dir_path and file_name
    expected_path = dir_path / file_name

    # Use the function to get the path
    result_path = get_file_path(dir_path, file_name)

    # Check if the result matches the expected path
    assert result_path == str(expected_path)


def test_check_file_exists(tmp_path):
    # Setup: create a temporary file
    test_file = tmp_path / "testfile.txt"
    test_file.touch()  # This creates the file

    # Test file exists
    assert check_file_exists(test_file) == True

    # Test file does not exist
    non_existent_file = tmp_path / "nonexistent.txt"
    with pytest.raises(FileNotFoundError) as e:
        check_file_exists(str(non_existent_file))
    assert str(e.value) == FileError.FILE_NOT_FOUND.value.format(
        file_path=non_existent_file
    )


def test_check_file_not_empty(tmp_path):
    # Setup: create a temporary file and write some data
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("Hello, World!")

    # Test file not empty

    assert check_file_not_empty(str(test_file)) == True

    # Test empty file
    empty_file = tmp_path / "emptyfile.txt"
    empty_file.touch()  # Create an empty file
    with pytest.raises(ValueError) as e:
        check_file_not_empty(str(empty_file))
    assert str(e.value) == FileError.FILE_IS_EMPTY.value.format(
        file_path=empty_file
    )
