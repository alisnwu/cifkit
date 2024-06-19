import pytest

from cifkit.data.mendeleeve_handler import get_mendeleev_nums_from_pair_tuple


@pytest.mark.fast
def test_get_mendeleev_num_from_tuple():
    pair = ("H", "Co")
    assert get_mendeleev_nums_from_pair_tuple(pair) == (92, 58)
