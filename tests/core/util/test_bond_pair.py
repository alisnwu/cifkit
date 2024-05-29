import pytest
from cifpy.utils.bond_pair import (
    get_possible_homogenous_element_pairs,
    get_possible_heterogenous_element_pairs,
)


@pytest.mark.parametrize(
    "formula, expected",
    [
        (
            "NaCl",
            [
                ("Cl", "Na")
            ],  # Ensure internal tuple order is consistent
        ),  # Binary example
        (
            "URhIn",
            [("In", "Rh"), ("In", "U"), ("Rh", "U")],
        ),  # Ternary example
        (
            "KNaClBr",
            [
                ("Br", "Cl"),
                ("Br", "K"),
                ("Br", "Na"),
                ("Cl", "K"),
                ("Cl", "Na"),
                ("K", "Na"),
            ],
        ),  # Quaternary example
    ],
)
def test_get_possible_homogenous_element_pairs(formula, expected):
    # Assuming the function sorts pairs alphabetically internally
    all_pairs = get_possible_heterogenous_element_pairs(formula)
    assert all_pairs == expected


@pytest.mark.parametrize(
    "formula_str, expected",
    [
        ("H2O", [("H", "H"), ("O", "O")]),
        ("CCl4", [("C", "C"), ("Cl", "Cl")]),
        ("Na2SO4", [("Na", "Na"), ("O", "O"), ("S", "S")]),
    ],
)
def test_get_possible_homogenous_element_pairs(formula_str, expected):
    result = get_possible_homogenous_element_pairs(formula_str)
    assert result == expected
