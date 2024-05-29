import numpy as np
import gemmi
from cifpy.util.cif_parser import trim_remove_braket
from gemmi.cif import Block


def get_coords_list(block: Block, loop_values: list):
    """
    Computes the new coordinates after applying
    symmetry operations to the initial coordinates.
    """

    loop_length = len(loop_values[0])
    coords_list = []
    for i in range(loop_length):
        atom_site_x = float(trim_remove_braket(loop_values[4][i]))
        atom_site_y = float(trim_remove_braket(loop_values[5][i]))
        atom_site_z = float(trim_remove_braket(loop_values[6][i]))
        atom_site_label = loop_values[0][i]

        coords_after_symmetry_operations = get_coords_after_sym_operations(
            block,
            [atom_site_x, atom_site_y, atom_site_z],
            atom_site_label,
        )
        coords_list.append(coords_after_symmetry_operations)

    return coords_list


def get_coords_after_sym_operations(
    block: Block,
    atom_site_fracs: list[float],
    atom_site_label: str,
) -> list[tuple[float, float, float, str]]:
    """
    Generates a list of coordinates for each atom site after applying
    symmetry operations.
    """
    all_coords = set()
    for operation in block.find_loop("_space_group_symop_operation_xyz"):
        operation = operation.replace("'", "")
        try:
            op = gemmi.Op(operation)
            new_x, new_y, new_z = op.apply_to_xyz(
                [
                    atom_site_fracs[0],
                    atom_site_fracs[1],
                    atom_site_fracs[2],
                ]
            )

            all_coords.add(
                (
                    round(new_x, 5),
                    round(new_y, 5),
                    round(new_z, 5),
                    atom_site_label,
                )
            )

        except RuntimeError as e:
            print(f"Skipping operation '{operation}': {str(e)}")
            raise RuntimeError(
                "An error occurred while processing symmetry operation"
            ) from e

    return list(all_coords)


def fractional_to_cartesian(
    fractional_coords: list[float],
    cell_lengths: list[float],
    rad_angles: list[float],
) -> list[float]:
    """
    Converts fractional coordinates to Cartesian
    coordinates using cell lengths and angles.
    """
    alpha, beta, gamma = rad_angles

    # Calculate the components of the transformation matrix
    a, b, c = cell_lengths
    cos_alpha = np.cos(alpha)
    cos_beta = np.cos(beta)
    cos_gamma = np.cos(gamma)
    sin_gamma = np.sin(gamma)

    # The volume of the unit cell
    volume = (
        a
        * b
        * c
        * np.sqrt(
            1
            - cos_alpha**2
            - cos_beta**2
            - cos_gamma**2
            + 2 * cos_alpha * cos_beta * cos_gamma
        )
    )

    # Transformation matrix from fractional to Cartesian coordinates
    matrix = np.array(
        [
            [a, b * cos_gamma, c * cos_beta],
            [
                0,
                b * sin_gamma,
                c * (cos_alpha - cos_beta * cos_gamma) / sin_gamma,
            ],
            [0, 0, volume / (a * b * sin_gamma)],
        ]
    )

    # Convert fractional coordinates to Cartesian coordinates
    fractional_coords = np.array(fractional_coords)
    if fractional_coords.ndim == 1:
        fractional_coords = fractional_coords[:, np.newaxis]

    cartesian_coords = np.dot(matrix, fractional_coords).flatten()
    print(cartesian_coords)

    return cartesian_coords
