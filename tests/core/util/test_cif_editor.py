import pytest
import shutil
import tempfile
import os
import filecmp

from cifkit.utils.cif_editor import (
    remove_author_loop,
)


@pytest.fixture
def setup_and_teardown_file():
    temp_dir = tempfile.mkdtemp()
    original_file_path = "tests/data/cif/format_author/author.cif"
    temp_file_path = os.path.join(temp_dir, "author.cif")
    reference_file_path = "tests/data/cif/format_author/author_removed.cif"

    shutil.copyfile(original_file_path, temp_file_path)
    yield temp_file_path, reference_file_path
    shutil.rmtree(temp_dir)


def test_remove_author_loop(setup_and_teardown_file):
    temp_file_path, reference_file_path = setup_and_teardown_file

    remove_author_loop(temp_file_path)

    assert filecmp.cmp(
        temp_file_path, reference_file_path, shallow=False
    ), "The modified file does not match the reference file."
