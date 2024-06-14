import pytest
from cifpy.coordination.method import compute_CN_max_gap_per_site


@pytest.mark.fast
def test_compute_CN_max_gap_per_site(
    radius_sum_data_URhIn, connections_URhIn, max_gaps_per_label_URhIn
):
    CN_max_gap_per_site = compute_CN_max_gap_per_site(
        radius_sum_data_URhIn,
        connections_URhIn,
        "full_occupancy",
    )

    assert CN_max_gap_per_site == max_gaps_per_label_URhIn


@pytest.mark.fast
def test_compute_CN_max_gap_per_site_dist_min_method_only(
    radius_sum_data_URhIn, connections_URhIn
):
    CN_max_gap_per_site = compute_CN_max_gap_per_site(
        radius_sum_data_URhIn,
        connections_URhIn,
        "full_occupancy_with_atomic_mixing",
    )

    assert CN_max_gap_per_site == {
        "In1": {"dist_by_shortest_dist": {"max_gap": 0.306, "CN": 14}},
        "U1": {"dist_by_shortest_dist": {"max_gap": 0.197, "CN": 11}},
        "Rh1": {"dist_by_shortest_dist": {"max_gap": 0.315, "CN": 9}},
        "Rh2": {"dist_by_shortest_dist": {"max_gap": 0.31, "CN": 9}},
    }
