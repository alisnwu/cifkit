import pytest

from cifpy.coordination.composition import (
    get_bond_counts_CN,
    get_bond_fraction_CN,
)


def test_get_atom_count_in_CN(formula_URhIn, connections_CN_URhIn):
    expected = {
        "In1": {("In", "In"): 4, ("In", "Rh"): 4, ("In", "U"): 6},
        "Rh1": {("In", "Rh"): 3, ("Rh", "U"): 6},
        "Rh2": {("In", "Rh"): 6, ("Rh", "U"): 3},
        "U1": {("In", "U"): 6, ("Rh", "U"): 5},
    }
    assert get_bond_counts_CN(formula_URhIn, connections_CN_URhIn) == expected


def test_get_bond_fraction_in_CN(bond_counts_CN):

    # Expected output based on input data
    expected_fractions = {
        ("In", "In"): 4 / 43,
        ("In", "Rh"): 13 / 43,
        ("In", "U"): 12 / 43,
        ("Rh", "U"): 14 / 43,
    }

    # Testing the actual function output
    result = get_bond_fraction_CN(bond_counts_CN)

    # Testing each bond fraction to ensure they are within a small tolerance
    for bond_type, expected_fraction in expected_fractions.items():
        assert pytest.approx(result[bond_type], 0.005) == expected_fraction

    # Testing to ensure the fractions sum approximately to 1
    assert pytest.approx(sum(result.values()), 0.005) == 1
