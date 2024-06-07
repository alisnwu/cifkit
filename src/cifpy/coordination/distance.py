def get_shortest_distance(connections: dict) -> float:
    """
    Return the shortest distance in the supercell.
    """
    min_dist = float("inf")

    # Iterate over each site's connections in the dictionary
    for label, connection_data in connections.items():
        if connection_data[0][1] < min_dist:
            min_dist = connection_data[0][1]

    # Check if the found minimum distance is less than the threshold
    return min_dist
