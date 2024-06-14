import numpy as np
from functools import partial
from scipy.optimize import minimize
from cifpy.data.radius import get_radius_data
from cifpy.utils.formula import get_unique_elements


def generate_adjacent_pairs(atom_labels):
    """
    Generate a list of tuples, where each tuple is
    a pair of adjacent atom labels.
    """

    # Binary -> [('In', 'Rh')]
    # Ternary -> [('In', 'Rh'), ('Rh', 'U')]
    label_to_pair = [
        (atom_labels[i], atom_labels[i + 1])
        for i in range(len(atom_labels) - 1)
    ]
    return label_to_pair


def objective(params, original_radii):
    """
    Calculate the objective function value,which is the sum of
    squared percent differences between original and refined radii.
    """

    return np.sum(((original_radii - params) / original_radii) ** 2)


def constraint(params, index_pair, shortest_distance):
    """
    Enforce that the sum of the radii of the pair does not
    exceed the shortest allowed distance between them.
    """
    i, j = index_pair
    i, j = index_pair
    return shortest_distance - (params[i] + params[j])


def optimize_CIF_radii(atom_labels, shortest_distances):
    """
    Optimize CIF radii given atom labels and their
    shortest pair distance constraints.
    """
    radii_data = get_radius_data()
    original_radii = np.array(
        [radii_data[label]["CIF_radius"] for label in atom_labels]
    )
    label_to_pair = generate_adjacent_pairs(atom_labels)

    # Constraints setup
    constraints = []
    for pair in label_to_pair:
        dist = shortest_distances[pair]
        print(
            f"Setting constraint for {pair[0]}-{pair[1]} with distance {dist}"
        )
        i, j = atom_labels.index(pair[0]), atom_labels.index(pair[1])
        constraints.append(
            {
                "type": "eq",
                "fun": partial(
                    constraint, index_pair=(i, j), shortest_distance=dist
                ),
            }
        )

    result = minimize(
        objective,
        original_radii,
        args=(original_radii,),
        constraints=constraints,
        options={"disp": True},
    )

    if result.success:
        print("Optimization succeeded.")
    else:
        print("Optimization failed:", result.message)

    return dict(zip(atom_labels, result.x)), result.fun
