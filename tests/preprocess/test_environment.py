from cifpy.preprocess.environment import get_all_labels_connections
from deepdiff import DeepDiff


def assert_minimum_distance(
    label, connections_dict, expected_min_distance
):
    """
    Asserts that the minimum distance for a given label in the
    connections dictionary matches the expected minimum distance.
    """
    connections = connections_dict.get(label, [])

    # Check if there are any connections, and calculate the minimum distance
    if connections:
        min_distance = min(
            connection[1] for connection in connections
        )
        assert min_distance == expected_min_distance


def test_get_nearest_dists_per_site_cooridnation_number(
    site_labels_URhIn,
    unitcell_points_URhIn,
    supercell_points_URhIn,
    angles_lenghts_URhIn,
):

    lengths, angles_rad = angles_lenghts_URhIn
    is_cn_used = True

    all_label_connections = get_all_labels_connections(
        site_labels_URhIn,
        unitcell_points_URhIn,
        supercell_points_URhIn,
        lengths,
        angles_rad,
        is_cn_used,
    )

    assert len(all_label_connections.get("In1")) == 14
    assert len(all_label_connections.get("U1")) == 11
    assert len(all_label_connections.get("Rh1")) == 9
    assert len(all_label_connections.get("Rh2")) == 9

    assert_minimum_distance("In1", all_label_connections, 2.697)
    assert_minimum_distance("U1", all_label_connections, 2.983)
    assert_minimum_distance("Rh1", all_label_connections, 2.852)
    assert_minimum_distance("Rh2", all_label_connections, 2.697)


def test_get_nearest_dists_per_site_cutoff_radius(
    site_labels_URhIn,
    unitcell_points_URhIn,
    supercell_points_URhIn,
    angles_lenghts_URhIn,
):

    lengths, angles_rad = angles_lenghts_URhIn
    is_cn_used = False

    all_label_connections = get_all_labels_connections(
        site_labels_URhIn,
        unitcell_points_URhIn,
        supercell_points_URhIn,
        lengths,
        angles_rad,
        is_cn_used,
        cutoff_radius=3.9,
    )

    assert len(all_label_connections.get("In1")) == 14
    assert len(all_label_connections.get("U1")) == 13
    assert len(all_label_connections.get("Rh1")) == 11
    assert len(all_label_connections.get("Rh2")) == 11

    assert_minimum_distance("In1", all_label_connections, 2.697)
    assert_minimum_distance("U1", all_label_connections, 2.983)
    assert_minimum_distance("Rh1", all_label_connections, 2.852)
    assert_minimum_distance("Rh2", all_label_connections, 2.697)
