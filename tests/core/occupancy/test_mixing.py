from cifkit.utils.cif_parser import get_loop_values, get_cif_block
from cifkit.occupacny.mixing import get_site_mixing_type
import pytest


def get_loop_values_from_cif(file_path):
    """
    Helper function to retrieve loop values from a CIF file.
    """
    cif_block = get_cif_block(file_path)
    return get_loop_values(cif_block)


def test_full_occupancy(loop_values_URhIn):
    file_mixing_type = get_site_mixing_type(loop_values_URhIn)
    assert file_mixing_type == "full_occupancy"


def test_deficiency_no_atomic_mixing():
    loop_values_deficiency = get_loop_values_from_cif(
        "tests/data/cif/occupancy/527000.cif"
    )
    file_mixing_type = get_site_mixing_type(loop_values_deficiency)
    assert file_mixing_type == "deficiency_no_atomic_mixing"


def test_full_occupancy_atomic_mixing():
    loop_values = get_loop_values_from_cif(
        "tests/data/cif/occupancy/529848.cif"
    )
    file_mixing_type = get_site_mixing_type(loop_values)

    assert file_mixing_type == "full_occupancy_atomic_mixing"


def test_deficiency_and_atomic_mixing():
    loop_values = get_loop_values_from_cif(
        "tests/data/cif/occupancy/554324.cif"
    )
    file_mixing_type = get_site_mixing_type(loop_values)
    assert file_mixing_type == "deficiency_atomic_mixing"
