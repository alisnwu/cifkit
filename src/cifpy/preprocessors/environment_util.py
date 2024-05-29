from cifpy.utils.string_parser import get_atom_type_from_label


def flat_site_connections(
    site_connections: dict,
) -> list[tuple[tuple[str, str], float]]:
    """
    Transform site connections into a sorted list of tuples, each containing
    a pair of alphabetically sorted elements and the distance.
    """
    flattened_points = []
    for site_label, connections in site_connections.items():
        for connection in connections:
            other_site_label = connection[0]
            distance = connection[1]
            site_element = get_atom_type_from_label(site_label)
            other_site_element = get_atom_type_from_label(
                other_site_label
            )
            # Sort the site label and other site label alphabetically
            element_pair = tuple(
                sorted((site_element, other_site_element))
            )
            flattened_points.append((element_pair, distance))

    flattened_points.sort(key=lambda x: x[0])
    return flattened_points


def find_minimum_dist_per_element_pair(
    flattened_connections: list[tuple[tuple[str, str], float]]
) -> dict[tuple[str, str], float]:
    """
    Determine the minimum distance for each unique pair of elements.
    """

    min_dist_per_element_pair = {}
    for connection in flattened_connections:
        element_pair = connection[0]
        distance = connection[1]
        if (
            element_pair not in min_dist_per_element_pair
            or distance < min_dist_per_element_pair[element_pair]
        ):
            min_dist_per_element_pair[element_pair] = distance

    return min_dist_per_element_pair
