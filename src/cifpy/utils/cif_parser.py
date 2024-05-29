"""
Parses attributes from a .cif file.
"""

import gemmi
from gemmi.cif import Block
from cifpy.utils.string_parser import trim_remove_braket
from cifpy.utils import unit
from cifpy.utils import error_messages


def get_cif_block(file_path: str) -> Block:
    """
    Return CIF block from file path.
    """
    doc = gemmi.cif.read_file(file_path)
    block = doc.sole_block()

    return block


def get_unitcell_lengths(
    block: Block,
) -> list[float]:
    """
    Return the unit cell lengths.
    """
    keys_lengths = [
        "_cell_length_a",
        "_cell_length_b",
        "_cell_length_c",
    ]

    lengths = [
        trim_remove_braket(block.find_value(key))
        for key in keys_lengths
    ]

    return lengths


def get_unitcell_angles_rad(
    block: Block,
) -> list[float]:
    """
    Return the unit cell angles.
    """

    keys_angles = [
        "_cell_angle_alpha",
        "_cell_angle_beta",
        "_cell_angle_gamma",
    ]

    angles = [
        trim_remove_braket(block.find_value(key))
        for key in keys_angles
    ]

    return unit.get_radians_from_degrees(angles)


def get_loop_tags() -> list[str]:
    """
    Return tags commonly used for atomic description.
    """
    loop_tags = [
        "_atom_site_label",
        "_atom_site_type_symbol",
        "_atom_site_symmetry_multiplicity",
        "_atom_site_Wyckoff_symbol",
        "_atom_site_fract_x",
        "_atom_site_fract_y",
        "_atom_site_fract_z",
        "_atom_site_occupancy",
    ]

    return loop_tags


def get_loop_values(block: Block) -> list[str]:
    """
    Retrieve a list of predefined loop tags for
    atomic site description.
    """
    loop_tags = get_loop_tags()

    loop_values = [block.find_loop(tag) for tag in loop_tags]

    # Check missing coordinates
    if (
        len(loop_values[4]) == 0
        or len(loop_values[5]) == 0
        or len(loop_values[6]) == 0
    ):
        raise ValueError(
            error_messages.CifParserError.MISSING_COORDINATES.value
        )

    return loop_values


def get_unique_label_count(loop_values: list) -> int:
    """
    Counts the number of labels in the loop.
    """
    return len(loop_values[0])


def get_unique_elements(loop_values: list) -> set[str]:
    """
    Returns a list of unique elements from loop values.
    """
    num_atom_labels = get_unique_label_count(loop_values)
    element_list = []
    for i in range(num_atom_labels):
        element = loop_values[1][i]
        element_list.append(str(element))
    return set(element_list)


def get_unique_site_labels(loop_values: list) -> list[str]:
    """
    Returns a list of atom labels from loop values.
    """
    num_atom_labels = get_unique_label_count(loop_values)
    label_list = []
    for i in range(num_atom_labels):
        element = loop_values[0][i]
        label_list.append(element)

    return label_list


def get_label_occupancy_coordinates(
    loop_values: list, i
) -> tuple[str, float, list[float, float, float]]:
    """
    Gets atom information (label, occupancy, coordinates) for the i-th atom.
    """
    label = loop_values[0][i]
    occupancy = trim_remove_braket(loop_values[7][i])
    coordinates = (
        trim_remove_braket(loop_values[4][i]),
        trim_remove_braket(loop_values[5][i]),
        trim_remove_braket(loop_values[6][i]),
    )

    return label, occupancy, coordinates


def get_loop_value_dict(loop_values: list) -> dict:
    """
    Create a dictionary containing CIF loop values for each label.
    """
    loop_value_dict = {}
    num_of_atom_labels = get_unique_label_count(loop_values)

    for i in range(num_of_atom_labels):
        label, occupancy, coordinates = (
            get_label_occupancy_coordinates(loop_values, i)
        )
        loop_value_dict[label] = {}
        loop_value_dict[label]["occupancy"] = occupancy
        loop_value_dict[label]["coords"] = coordinates

    return loop_value_dict


def get_start_end_line_indexes(
    file_path: str, start_keyword: str
) -> tuple[int, int]:
    """
    Find the starting and ending indexes of the lines in atom_site_loop
    """

    with open(file_path, "r") as f:
        lines = f.readlines()

    start_index = None
    end_index = None

    # Find the start index
    for i, line in enumerate(lines):
        if start_keyword in line:
            start_index = i + 1
            break

    if start_index is None:
        return None, None

    # Find the end index
    for i in range(start_index, len(lines)):
        if lines[i].strip() == "":
            end_index = i
            break

    return start_index, end_index


def get_line_content_from_tag(
    file_path: str, start_keyword: str
) -> list[str]:
    """
    Returns a list containing file content with starting keyword.
    """
    start_index, end_index = get_start_end_line_indexes(
        file_path, start_keyword
    )

    if start_index is None or end_index is None:
        print("Section starting with", start_keyword, "not found.")
        return None

    with open(file_path, "r") as f:
        lines = f.readlines()

    # Extract the content between start_index and end_index
    content_lines = lines[start_index:end_index]

    return content_lines
