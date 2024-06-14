import numpy as np
import pytest
from cifpy.data.radius_optimization import (
    optimize_CIF_radii,
    generate_adjacent_pairs,
)


@pytest.mark.fast
def test_optimization(cif_URhIn):

    # Example usage:
    elements_sorted = sorted(cif_URhIn.unique_elements)
    assert elements_sorted == ["In", "Rh", "U"]
    assert cif_URhIn.shortest_dist_per_bond_pair == {
        ("In", "In"): 3.244,
        ("In", "Rh"): 2.697,  # RM
        ("In", "U"): 3.21,
        ("Rh", "Rh"): 3.881,
        ("Rh", "U"): 2.983,  # MX
        ("U", "U"): 3.881,
    }
    optimized_radii, objective_value = optimize_CIF_radii(
        elements_sorted, cif_URhIn.shortest_dist_per_bond_pair
    )

    expected_radii = np.array([1.614, 1.369, 1.328])
    optimized_radii_values = np.array(
        [optimized_radii["U"], optimized_radii["Rh"], optimized_radii["In"]]
    )

    # Use numpy's testing function to assert closeness
    assert optimized_radii_values == pytest.approx(
        expected_radii, abs=1e-3, rel=1e-3
    )
