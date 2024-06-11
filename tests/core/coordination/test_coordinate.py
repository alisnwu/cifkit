import numpy as np
from cifpy.coordination.coordinate import get_polyhedron_coordinates_labels


def test_get_polyhedron_coordinates_label(connections_CN_URhIn):
    expected_labels = [
        "Rh2",
        "Rh2",
        "Rh1",
        "Rh1",
        "U1",
        "U1",
        "In1",
        "In1",
        "U1",
        "U1",
        "U1",
        "U1",
        "In1",
        "In1",
        "In1",
    ]

    polyhedron_points, labels = get_polyhedron_coordinates_labels(
        connections_CN_URhIn, "In1"
    )
    assert len(polyhedron_points) == 15
    assert labels == expected_labels
