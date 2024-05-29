import pandas as pd
from cifpy.data.mendeleev import get_mendeleev_numbers
from cifpy.utils import string_parser


def order_pair_by_mendeleev(label_pair_tuple: tuple[str, str]):
    """
    Order atomic label tuples based on Mendeleev numbers.
    """
    first_label, second_label = label_pair_tuple

    first_mendeleev_num, second_mendeleev_num = (
        get_mendeleev_num_from_pair(label_pair_tuple)
    )

    if first_mendeleev_num > second_mendeleev_num:
        return (second_label, first_label)
    # If the Mendeleev numbers are the same, sort the labels alphabetically
    elif first_mendeleev_num == second_mendeleev_num:
        return sort_label_tuple(label_pair_tuple)
    # If they are in the correct order, return the tuple as it is
    else:
        return label_pair_tuple


def get_mendeleev_num_from_pair(
    pair_tuple: tuple[str, str]
) -> tuple[int, int]:
    """
    Parse the Mendeleev number for each element in the tuple.
    """
    first_element = string_parser.get_atom_type_from_label(
        pair_tuple[0]
    )
    second_element = string_parser.get_atom_type_from_label(
        pair_tuple[1]
    )
    # Retrieve Mendeleev numbers from the dictionary using the elements in the tuple
    mendeleev_numbers = get_mendeleev_numbers
    first_mendeleev_num = mendeleev_numbers[first_element]
    second_mendeleev_num = mendeleev_numbers[second_element]

    return first_mendeleev_num, second_mendeleev_num


def sort_label_tuple(strings: tuple[str, str]):
    """
    Sort a tuple of strings alphabetically.
    """
    return tuple(sorted(strings))
