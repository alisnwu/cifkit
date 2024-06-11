import pytest
import numpy as np
from cifpy.utils.unit import (
    get_radians_from_degrees,
    round_float,
    fractional_to_cartesian,
)


def test_get_radians_from_degrees():
    # Define the input and expected output
    angles_in_degrees = [0, 45, 90, 180, 360]
    expected_radians = [0.0, 0.7854, 1.5708, 3.14159, 6.28319]

    # Call the function and check the output
    result = get_radians_from_degrees(angles_in_degrees)
    assert result == expected_radians


def test_rounded_distance():
    # Define the input and expected output
    distance = 123.456789
    expected_rounded = 123.457

    # Call the function and check the output
    result = round_float(distance)
    assert result == expected_rounded

    # Test with different precision
    distance = 123.456789
    precision = 4
    expected_rounded = 123.4568
    result = round_float(distance, precision)
    assert result == expected_rounded


def test_fractional_to_cartesian():
    frac_pts = [0.2505, 0, 0.5]
    lengths = [7.476, 7.476, 3.881]
    angles = [90, 90, 120]
    angles_rad = get_radians_from_degrees(angles)

    # Expected cartesian coordinates
    expected_cart = [1.87273087, -1.23458760e-05, 1.94050000]

    # Actual cartesian coordinates from function
    cart_1 = fractional_to_cartesian(frac_pts, lengths, angles_rad)
    assert np.allclose(
        cart_1, expected_cart, atol=1e-4
    ), f"Expected {expected_cart}, but got {cart_1}"