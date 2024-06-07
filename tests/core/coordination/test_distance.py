from cifpy.coordination.distance import (
    get_shortest_distance,
    is_min_dist_shorter,
)


def test_get_shortest_distance(site_connections_URhIn):
    assert get_shortest_distance(site_connections_URhIn) == 2.697


def is_min_dist_shorter(site_connections_URhIn):
    assert is_min_dist_shorter(site_connections_URhIn, 3.00)
    assert is_min_dist_shorter(site_connections_URhIn, 2.50) == False
