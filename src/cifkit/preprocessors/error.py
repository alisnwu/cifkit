import os
from cifkit.utils import folder
import glob
from cifkit.models.cif import Cif
from cifkit.utils.error_messages import CifParserError
from pathlib import Path


def make_directory_and_move(file_path, dir_path, new_file_path):
    """Create directory if it doesn't exist and move the file."""
    os.makedirs(dir_path, exist_ok=True)
    new_file_path = os.path.join(dir_path, new_file_path)
    os.rename(file_path, new_file_path)


def move_files_based_on_errors(dir_path):
    print("\nCIF Preprocessing has begun...\n")

    # Ensure dir_path is a Path object
    dir_path = Path(dir_path)

    # Dictionary to hold directory paths for each error type
    error_directories = {
        CifParserError.SYMMETRY_OPERATION_ERROR: dir_path / "bad_op",
        CifParserError.WRONG_LOOP_VALUE_COUNT: dir_path / "wrong_loop_value",
        CifParserError.MISSING_COORDINATES: dir_path / "bad_coords",
        CifParserError.INVALID_PARSED_ELEMENT: dir_path / "invalid_label",
        CifParserError.DUPLICATE_LABELS: dir_path / "duplicate_labels",
        "other_error": dir_path / "other_error",
    }

    # Ensure all direct
    num_files = {key.value: 0 for key in CifParserError}
    num_files["other_error"] = 0

    file_paths = folder.get_file_paths(str(dir_path))

    for file_path in file_paths:
        filename = os.path.basename(file_path)
        moved = False

        try:
            Cif(file_path)
        except Exception as e:
            error_message = str(e)
            for error, message in CifParserError.__members__.items():
                if message.value in error_message:
                             
                    make_directory_and_move(
                        file_path, error_directories[message], filename
                    )
                    num_files[message.value] += 1
                    moved = True
                    break

            if not moved:
                make_directory_and_move(
                    file_path, error_directories["other_error"], filename
                )
                num_files["other_error"] += 1

            print(f"File {filename} moved due to error: {error_message}")
    print(num_files)
