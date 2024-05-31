from cifpy.utils.string_parser import get_atom_type_from_label


def flat_site_connections(
    site_connections: dict,
):
    """
    Transform site connections into a sorted list of tuples,
    each containing a pair of alphabetically sorted elements and the distance.
    """
    flattened_points = []
    for site_label, connections in site_connections.items():
        for connection in connections:
            other_site_label = connection[0]
            distance = connection[1]
            site_element = get_atom_type_from_label(site_label)
            other_site_element = get_atom_type_from_label(other_site_label)
            # Sort the site label and other site label alphabetically
            element_pair = tuple(sorted((site_element, other_site_element)))
            flattened_points.append((element_pair, distance))

    flattened_points.sort(key=lambda x: x[0])
    return flattened_points
