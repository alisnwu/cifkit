from cifpy.utils.string_parser import get_atom_type_from_label
from cifpy.utils import bond_pair


def get_bond_counts_CN(formula: str, connections: dict[str, list]) -> dict:
    """
    Return a dictionary containing bond pairs and counts per label site.
    """
    all_bond_pairs = bond_pair.get_all_bond_pairs(formula)

    # Initialize the dictionary to hold bond pair counts for each label
    bond_pair_data: dict = {}

    # Iterate over each label and its connections
    for label, label_connections in connections.items():
        # Initialize the bond count for the current label
        bond_pair_data[label] = {}

        # Get the atom type for the reference label
        ref_element = get_atom_type_from_label(label)

        # Iterate over each connection for the current label
        for conn in label_connections:
            conn_label, _, _, _, _ = conn

            # Get the atom type for the connected label
            conn_element = get_atom_type_from_label(conn_label)

            # Create a tuple representing the bond pair, sorted
            sorted_bond_pair = tuple(sorted((ref_element, conn_element)))

            # Check if the bond pair is one of the valid pairs
            if sorted_bond_pair in all_bond_pairs:
                if sorted_bond_pair in bond_pair_data[label]:
                    bond_pair_data[label][sorted_bond_pair] += 1
                else:
                    bond_pair_data[label][sorted_bond_pair] = 1

    return bond_pair_data


def get_bond_fraction_CN(bond_pair_data: dict) -> dict[tuple[str, str], float]:
    """
    Calculate the fraction of each bond type across all labels.
    """
    total_bond_counts: dict[tuple[str, str], float] = {}
    total_bonds = 0

    # Sum up bond counts for each bond type
    for bonds in bond_pair_data.values():
        for bond_type, count in bonds.items():
            if bond_type in total_bond_counts:
                total_bond_counts[bond_type] += count
            else:
                total_bond_counts[bond_type] = count
            total_bonds += count

    # Calculate fractions
    bond_fractions = {
        bond_type: round(count / total_bonds, 3)
        for bond_type, count in total_bond_counts.items()
    }

    return bond_fractions
