import pytest
import numpy as np
from cifpy.util.unit import (
    get_radians_from_degrees,
    round_float,
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
