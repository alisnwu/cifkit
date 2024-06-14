import numpy as np


def get_CN_connections(best_polyhedrons, all_labels_connections):
    """
    Retrieve connections limited by the number of vertices (CN_value)
    for each label.
    """
    CN_connections = {}

    for label, data in best_polyhedrons.items():
        CN_value = data[
            "number_of_vertices"
        ]  # Extract the limit for the number of vertices
        # Limit the connections for this label using CN_value
        CN_connections[label] = all_labels_connections[label][:CN_value]

    return CN_connections