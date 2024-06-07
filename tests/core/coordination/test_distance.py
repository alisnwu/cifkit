from cifpy.coordination.distance import (
    get_shortest_distance,
)


def test_get_shortest_distance(site_connections_URhIn):
    assert get_shortest_distance(site_connections_URhIn) == 2.697
