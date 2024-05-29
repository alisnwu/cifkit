import numpy as np
from cifpy.util import unit
import difflib
import pprint


from cifpy.preprocess.supercell import (
    get_coords_after_sym_operations,
    fractional_to_cartesian,
    get_coords_list,
)


def test_get_unit_cell_coordinates(cif_block_URhIn, loop_values_URhIn):
    coordinates = get_coords_list(cif_block_URhIn, loop_values_URhIn)
    # Flatten the coordinates for comparision with the expected
    coordinates_set = set(
        tuple(coord) for sublist in coordinates for coord in sublist
    )
    expected_set = set(
        (
            (-0.2505, -0.2505, 0.5, "In1"),
            (0.0, 0.2505, 0.5, "In1"),
            (0.2505, 0.0, 0.5, "In1"),
            (-0.2505, -0.2505, -0.5, "In1"),
            (0.0, 0.2505, -0.5, "In1"),
            (0.2505, 0.0, -0.5, "In1"),
            (0.5925, 0.0, 0.0, "U1"),
            (-0.5925, -0.5925, 0.0, "U1"),
            (0.0, 0.5925, 0.0, "U1"),
            (0.33333, -0.33333, -0.5, "Rh1"),
            (0.66667, 0.33333, -0.5, "Rh1"),
            (0.33333, 0.66667, -0.5, "Rh1"),
            (-0.33333, 0.33333, 0.5, "Rh1"),
            (-0.66667, -0.33333, 0.5, "Rh1"),
            (-0.33333, -0.66667, -0.5, "Rh1"),
            (-0.33333, -0.66667, 0.5, "Rh1"),
            (-0.66667, -0.33333, -0.5, "Rh1"),
            (0.33333, -0.33333, 0.5, "Rh1"),
            (-0.33333, 0.33333, -0.5, "Rh1"),
            (0.66667, 0.33333, 0.5, "Rh1"),
            (0.33333, 0.66667, 0.5, "Rh1"),
            (0.0, 0.0, 0.0, "Rh2"),
        )
    )

    # Compare the two sets
    assert (
        coordinates_set == expected_set
    ), f"Expected {expected_set}, but got {coordinates_set}"


def test_fractional_to_cartesian():
    frac_pts = [0.2505, 0, 0.5]
    lengths = [7.476, 7.476, 3.881]
    angles = [90, 90, 120]
    angles_rad = unit.get_radians_from_degrees(angles)

    # Expected cartesian coordinates
    expected_cart = [1.87273087, -1.23458760e-05, 1.94050000]

    # Actual cartesian coordinates from function
    cart_1 = fractional_to_cartesian(frac_pts, lengths, angles_rad)
    assert np.allclose(
        cart_1, expected_cart, atol=1e-4
    ), f"Expected {expected_cart}, but got {cart_1}"
