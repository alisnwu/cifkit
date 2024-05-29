# conftest.py
import pytest
from cifpy.util import cif_parser


@pytest.fixture(scope="module")
def file_path_URhIn():
    return "tests/data/cif/URhIn.cif"


@pytest.fixture(scope="module")
def cif_block_URhIn(file_path_URhIn):
    return cif_parser.get_cif_block(file_path_URhIn)


@pytest.fixture(scope="module")
def loop_values_URhIn(cif_block_URhIn):
    return cif_parser.get_loop_values(cif_block_URhIn)
