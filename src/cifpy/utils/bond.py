from itertools import product


def get_all_ordered_pairs_from_list(elements):
    """
    Generates all possible unique ordered pairs following a specific order.
    """

    # Generate all possible pairs (with ordering matter)
    all_pairs = list(product(elements, repeat=2))

    return all_pairs
