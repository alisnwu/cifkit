# conftest.py
import pytest
import sys
from cifpy.preprocessors import (
    supercell,
    environment,
    environment_util,
)
from cifpy.utils import cif_parser


@pytest.fixture(scope="module")
def file_path_URhIn():
    return "tests/data/cif/URhIn.cif"


@pytest.fixture(scope="module")
def formula_URhIn():
    return "URhIn"


@pytest.fixture(scope="module")
def cif_block_URhIn(file_path_URhIn):
    return cif_parser.get_cif_block(file_path_URhIn)


@pytest.fixture(scope="module")
def unique_site_labels_URhIn(loop_values_URhIn):
    return cif_parser.get_unique_site_labels(loop_values_URhIn)


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
def lenghts_URhIn(cif_block_URhIn) -> list[float]:
    lenghts = cif_parser.get_unitcell_lengths(cif_block_URhIn)
    return lenghts


@pytest.fixture(scope="module")
def angles_rad_URhIn(cif_block_URhIn) -> list[float]:
    angles_rad = cif_parser.get_unitcell_angles_rad(cif_block_URhIn)
    return angles_rad


@pytest.fixture(scope="module")
def site_labels_URhIn(loop_values_URhIn):
    return cif_parser.get_unique_site_labels(loop_values_URhIn)


@pytest.fixture(scope="module")
def parsed_cif_data_URhIn(
    unique_site_labels_URhIn, lenghts_URhIn, angles_rad_URhIn
) -> tuple[list[str], list[float], list[float]]:
    return (unique_site_labels_URhIn, lenghts_URhIn, angles_rad_URhIn)


@pytest.fixture(scope="module")
def site_connections_URhIn(
    parsed_cif_data_URhIn,
    unitcell_points_URhIn,
    supercell_points_URhIn,
):

    return environment.get_site_connections(
        parsed_cif_data_URhIn,
        unitcell_points_URhIn,
        supercell_points_URhIn,
        False,
    )


@pytest.fixture(scope="module")
def flattened_connections_URhIn(site_connections_URhIn):
    return environment_util.flat_site_connections(
        site_connections_URhIn
    )
