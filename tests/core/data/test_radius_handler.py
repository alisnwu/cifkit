import pytest
from cifpy.data.radius_handler import (
    get_CIF_pauling_radii,
    merge_refined_CIF_radii,
    compute_pair_distances,
)


@pytest.mark.fast
def test_get_CIF_pauling_radii():
    test_elements = ["Si", "Fe"]
    expected = {
        "Fe": {"CIF": 1.242, "Pauling": 1.26},
        "Si": {"CIF": 1.176, "Pauling": 1.316},
    }
    assert get_CIF_pauling_radii(test_elements) == expected

    test_elements = ["In", "Rh", "U"]
    expected = {
        "In": {"CIF": 1.624, "Pauling": 1.66},
        "Rh": {"CIF": 1.345, "Pauling": 1.342},
        "U": {"CIF": 1.377, "Pauling": 1.51},
    }
    assert get_CIF_pauling_radii(test_elements) == expected


@pytest.mark.fast
def test_get_CIF_pauling_radii(radii_data_URhIn):
    test_elements = ["In", "Rh", "U"]
    shorest_distance_per_bond = {
        ("In", "In"): 3.244,
        ("In", "Rh"): 2.697,  # RM
        ("In", "U"): 3.21,
        ("Rh", "Rh"): 3.881,
        ("Rh", "U"): 2.983,  # MX
        ("U", "U"): 3.881,
    }
    combined_radii = merge_refined_CIF_radii(
        test_elements, shorest_distance_per_bond
    )
    expected = {
        "In": {
            "CIF_radius": 1.624,
            "CIF_radius_refined": 1.3283,
            "Pauling_radius_CN12": 1.66,
        },
        "Rh": {
            "CIF_radius": 1.345,
            "CIF_radius_refined": 1.3687,
            "Pauling_radius_CN12": 1.342,
        },
        "U": {
            "CIF_radius": 1.377,
            "CIF_radius_refined": 1.6143,
            "Pauling_radius_CN12": 1.51,
        },
    }

    # Assert each element and sub-element individually
    for element, radii in expected.items():
        for key, value in radii.items():
            assert combined_radii[element][key] == pytest.approx(
                value, abs=0.001
            )


@pytest.mark.fast
def test_compute_pair_distances(radii_data_URhIn):
    result = compute_pair_distances(radii_data_URhIn)
    print(result)
    expected = {
        "CIF_radius_sum": {
            "In-In": 3.248,
            "In-Rh": 2.969,
            "In-U": 3.001,
            "Rh-Rh": 2.69,
            "Rh-U": 2.722,
            "U-U": 2.754,
        },
        "CIF_radius_refined_sum": {
            "In-In": 2.657,
            "In-Rh": 2.697,
            "In-U": 2.943,
            "Rh-Rh": 2.737,
            "Rh-U": 2.983,
            "U-U": 3.229,
        },
        "Pauling_radius_sum": {
            "In-In": 3.32,
            "In-Rh": 3.002,
            "In-U": 3.17,
            "Rh-Rh": 2.684,
            "Rh-U": 2.852,
            "U-U": 3.02,
        },
    }

    assert result == expected
