import pytest
from cifpy.utils.sort import order_pair_by_mendeleev


# # U = 20, In = 75, already in order
# @pytest.mark.parametrize(
#     "input_pair,expected_output",
#     [
#         (("In", "U"), ("U", "In")),
#         (("U", "In"), ("U", "In")),
#         (("Rh", "U"), ("U", "Rh")),
#         (("In", "Rh"), ("Rh", "In")),
#         (("Rh4", "Rh2"), ("Rh2", "Rh4")),
#         (("Co2B", "Co2A"), ("Co2A", "Co2B")),
#         (("Co2A", "Co2B"), ("Co2A", "Co2B")),
#     ],
# )
# def test_order_pair_by_mendeleev(input_pair, expected_output):
#     result = order_pair_by_mendeleev(input_pair)
#     assert result == expected_output
