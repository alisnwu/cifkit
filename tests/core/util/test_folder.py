import pytest
from pathlib import Path
import os
from cifpy.utils.folder import (
    get_file_path,
    get_file_count,
    get_file_path_list,
    make_output_folder,
    check_file_exists,
    check_file_not_empty,
    move_files,
    copy_files,
)
from cifpy.utils.error_messages import FileError


def test_get_file_count(cif_folder_path_test):
    count = get_file_count(cif_folder_path_test, ext=".cif")
    assert count == 3


def test_get_file_path_list(cif_folder_path_test):
    expected_files = {"300169.cif", "300170.cif", "300171.cif"}
    file_paths = get_file_path_list(cif_folder_path_test, ext=".cif")
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


def test_move_files(tmp_path, cif_folder_path_test, file_paths_test):
    dest_dir = tmp_path / "destination"
    # Initial file count in the source directory
    initial_file_count = get_file_count(cif_folder_path_test)

    # Move files to the destination directory
    move_files(dest_dir, file_paths_test)

    # Check the file count in the source directory after move
    assert get_file_count(cif_folder_path_test) == initial_file_count - len(
        file_paths_test
    )
    # Move files back to the original source directory
    move_files(str(cif_folder_path_test), get_file_path_list(str(dest_dir)))

    # Final file count in the source directory
    final_file_count = get_file_count(cif_folder_path_test)
    assert final_file_count == initial_file_count


def test_copy_files(tmp_path, cif_folder_path_test, file_paths_test):
    dest_dir = tmp_path / "destination"
    dest_dir.mkdir()  # Ensure destination directory exists

    # Copy files to the destination directory
    copy_files(str(dest_dir), file_paths_test)

    # Retrieve lists of file paths in both directories
    source_files = get_file_path_list(cif_folder_path_test)
    destination_files = get_file_path_list(str(dest_dir))

    # Extract basenames and sort to ensure order does not affect comparison
    source_basenames = sorted(
        [Path(file_path).name for file_path in source_files]
    )
    destination_basenames = sorted(
        [Path(file_path).name for file_path in destination_files]
    )

    # Check the basenames in the source directory match those in the destination
    assert source_basenames == destination_basenames
