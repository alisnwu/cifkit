from cifpy.coordination.composition import get_bond_counts_in_CN


def test_get_atom_count_in_CN(formula_URhIn, connections_CN_URhIn):
    expected = {
        "In1": {("In", "In"): 4, ("In", "Rh"): 4, ("In", "U"): 6},
        "Rh1": {("In", "Rh"): 3, ("Rh", "U"): 6},
        "Rh2": {("In", "Rh"): 6, ("Rh", "U"): 3},
        "U1": {("In", "U"): 6, ("Rh", "U"): 5},
    }
    assert (
        get_bond_counts_in_CN(formula_URhIn, connections_CN_URhIn) == expected
    )
