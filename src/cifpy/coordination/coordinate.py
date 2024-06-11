import numpy as np


def get_polyhedron_coordinates_labels(
    connections: dict, label: str
) -> tuple[list[list[float]], list[str]]:
    """Return a list of Cartesian coordinates and labels. The central atom is
    the last element."""
    conn_data = connections[label]
    polyhedron_points = [conn[3] for conn in conn_data]
    vertex_labels = [conn[0] for conn in conn_data]

    # Parse centerl atom information
    central_atom_coord = conn_data[0][2]
    central_atom_label = label
    polyhedron_points.append(central_atom_coord)
    vertex_labels.append(central_atom_label)
    return polyhedron_points, vertex_labels
