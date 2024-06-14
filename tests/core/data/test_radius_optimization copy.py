import pytest
from cifpy.data.radius_optimization import (
    optimize_CIF_radii,
)


@pytest.mark.fast
def test_optimization(cif_URhIn):

    # Example usage:
    atom_labels = ["In", "Rh", "U"]
    print(cif_URhIn.shortest_dist_per_bond_pair)

    shortest_distances = {
        ("In", "In"): 3.244,
        ("In", "Rh"): 2.697,  # RM
        ("In", "U"): 3.21,
        ("Rh", "Rh"): 3.881,
        ("Rh", "U"): 2.983,  # MX
        ("U", "U"): 3.881,
    }

    optimized_radii, objective_value = optimize_CIF_radii(
        atom_labels, shortest_distances
    )
    print("Optimized Radii:", optimized_radii)
    print("Objective Value:", objective_value)

    # Example usage:


# @pytest.mark.fast
# def test_optimization(cif_URhIn):

#     # Example usage:
#     elements = list(cif_URhIn.unique_elements)
#     optimized_radii, objective_value = optimize_CIF_radii(
#         elements, cif_URhIn.shortest_dist_per_bond_pair
#     )
#     print("Optimized Radii:", optimized_radii)
#     print("Objective Value:", objective_value)
#     # Expected values for the radii in the order of 'U', 'Rh', 'In'
#     expected_radii = np.array([1.614, 1.369, 1.328])

#     optimized_radii_values = np.array(
#         [optimized_radii["U"], optimized_radii["Rh"], optimized_radii["In"]]
#     )

#     # Using np.testing.assert_allclose to compare with tolerance
#     np.testing.assert_allclose(
#         optimized_radii_values, expected_radii, atol=1e-3, rtol=1e-3
#     )


# """
