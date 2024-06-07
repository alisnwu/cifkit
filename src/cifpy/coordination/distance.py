def get_shortest_distance(connections: dict) -> float:
    """
    Return the shortest distance in the supercell.
    """
    min_dist = float("inf")
    # Iterate over each site's connections in the dictionary
    for label, connection_data in connections.items():
        min_dist = connection_data[0][1]

    # Check if the found minimum distance is less than the threshold
    return min_dist


def is_min_dist_shorter(connections: dict, dist_threshold: float) -> bool:
    return get_shortest_distance(connections) < dist_threshold
    """
    Return true if the shortest pair distance in the connection
    is shorter than the distance value provided.
    """
