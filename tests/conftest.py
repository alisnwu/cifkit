# conftest.py
import pytest
import sys
from cifpy.preprocess import supercell
from cifpy.util import cif_parser, unit


@pytest.fixture(scope="module")
def file_path_URhIn():
    return "tests/data/cif/URhIn.cif"


@pytest.fixture(scope="module")
def cif_block_URhIn(file_path_URhIn):
    return cif_parser.get_cif_block(file_path_URhIn)


@pytest.fixture(scope="module")
def loop_values_URhIn(cif_block_URhIn):
    return cif_parser.get_loop_values(cif_block_URhIn)


@pytest.fixture(scope="module")
def unitcell_coords_URhIn(cif_block_URhIn):
    return supercell.get_unitcell_coords_for_all_labels(
        cif_block_URhIn
    )


@pytest.fixture(scope="module")
def unitcell_points_URhIn(cif_block_URhIn):
    return supercell.get_supercell_points(cif_block_URhIn, 1)


@pytest.fixture(scope="module")
def supercell_points_URhIn(cif_block_URhIn):
    return supercell.get_supercell_points(cif_block_URhIn, 3)


@pytest.fixture(scope="module")
def angles_lenghts_URhIn(cif_block_URhIn):
    lenghts, angles = cif_parser.parse_unit_cell_lengths_angles(
        cif_block_URhIn
    )
    return lenghts, unit.get_radians_from_degrees(angles)


@pytest.fixture(scope="module")
def site_labels_URhIn(loop_values_URhIn):
    return cif_parser.get_atom_label_list(loop_values_URhIn)
