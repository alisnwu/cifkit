import pytest
from cifpy.data.radius_handler import (
    get_CIF_pauling_radius,
    get_radius_values_per_element,
    compute_radius_sum,
    get_is_radius_data_available,
)


@pytest.mark.fast
def test_get_CIF_pauling_radii():
    test_elements = ["Si", "Fe"]
    expected = {
        "Fe": {"CIF": 1.242, "Pauling": 1.26},
        "Si": {"CIF": 1.176, "Pauling": 1.316},
    }
    assert get_CIF_pauling_radius(test_elements) == expected

    test_elements = ["In", "Rh", "U"]
    expected = {
        "In": {"CIF": 1.624, "Pauling": 1.66},
        "Rh": {"CIF": 1.345, "Pauling": 1.342},
        "U": {"CIF": 1.377, "Pauling": 1.51},
    }
    assert get_CIF_pauling_radius(test_elements) == expected


@pytest.mark.fast
def test_get_CIF_pauling_radii(radius_data_URhIn):
    test_elements = ["In", "Rh", "U"]
    shorest_distance_per_bond = {
        ("In", "In"): 3.244,
        ("In", "Rh"): 2.697,  # RM
        ("In", "U"): 3.21,
        ("Rh", "Rh"): 3.881,
        ("Rh", "U"): 2.983,  # MX
        ("U", "U"): 3.881,
    }
    combined_radii = get_radius_values_per_element(
        test_elements, shorest_distance_per_bond
    )
    expected = radius_data_URhIn

    # Assert each element and sub-element individually
    for element, radii in expected.items():
        for key, value in radii.items():
            assert combined_radii[element][key] == pytest.approx(
                value, abs=0.001
            )


@pytest.mark.fast
def test_compute_radius_sum(radius_data_URhIn, radius_sum_data_URhIn):
    result = compute_radius_sum(radius_data_URhIn)
    expected = radius_sum_data_URhIn
    assert result == expected


@pytest.mark.parametrize(
    "elements,expected",
    [
        (["H", "Li"], False),
        (["H", "He"], False),
        (["Be"], False),
        (["U", "Rh", "In"], True),
        (["Er", "Co", "In"], True),
    ],
)
@pytest.mark.fast
def test_check_radius_data_available(elements, expected):
    assert get_is_radius_data_available(elements) == expected
