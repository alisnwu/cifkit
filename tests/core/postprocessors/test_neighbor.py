from cifpy.postprocessors.neighbor import (
    get_min_distance_pair,
    get_heterogenous_bond_dists,
)

from cifpy.utils import bond_pair


def test_get_min_distance_pair(site_connections_URhIn):
    """
    Return the shortest distance
    """
    min_dist_tuple = get_min_distance_pair(site_connections_URhIn)
    assert min_dist_tuple == (("In", "Rh"), 2.697)


def test_get_heterogenous_bond_dists(
    site_connections_URhIn, formula_URhIn
):

    heterogenous_bond_connetions = get_heterogenous_bond_dists(
        site_connections_URhIn, formula_URhIn
    )
    # assert heterogenous_bond_connetions == {}


# for label_type, connections in all_labels_connections.items():
#         for connetion in connections:
#             ref_atom_type = cif_parser.get_atom_type(label_type)
#             other_atom_type = cif_parser.get_atom_type(connetion[0])
#             dist = connetion[1]
