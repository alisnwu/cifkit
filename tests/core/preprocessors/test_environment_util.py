from cifpy.preprocessors.environment_util import (
    flat_site_connections,
    find_minimum_dist_per_element_pair,
)


def test_flat_connections(site_connections_URhIn):
    flattened_connections = flat_site_connections(
        site_connections_URhIn
    )

    assert isinstance(flattened_connections, list)
    for connection in flattened_connections:
        assert (
            isinstance(connection, tuple) and len(connection) == 2
        ), "Each item should be a tuple with two elements."
        assert (
            isinstance(connection[0], tuple)
            and len(connection[0]) == 2
        ), "First element of each item should be a tuple of two strings."
        assert isinstance(
            connection[1], float
        ), "Second element of each item should be a float."
        assert all(
            isinstance(label, str) for label in connection[0]
        ), "Both elements in the label tuple should be strings."


def test_find_minimum_dist_per_element_pair(
    flattened_connections_URhIn,
):

    # Call the function under test
    min_dist_per_element_pair = find_minimum_dist_per_element_pair(
        flattened_connections_URhIn
    )

    # Assert that the actual minimum distances match the expected results
    assert min_dist_per_element_pair == {
        ("In", "In"): 3.244,
        ("In", "Rh"): 2.697,
        ("In", "U"): 3.21,
        ("Rh", "Rh"): 3.881,
        ("Rh", "U"): 2.983,
        ("U", "U"): 3.881,
    }
