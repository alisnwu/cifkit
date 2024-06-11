"""
Parses attributes from a .cif file.
"""

import gemmi
from typing import Any
from gemmi.cif import Block, Column
from cifpy.utils.string_parser import (
    get_string_to_formatted_float,
    trim_string,
    get_atom_type_from_label,
    clean_parsed_structure,
)
from cifpy.utils import unit
from cifpy.utils.error_messages import CifParserError


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
        get_string_to_formatted_float(block.find_value(key))
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
        get_string_to_formatted_float(block.find_value(key))
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


def get_loop_values(block: Block) -> list[Column]:
    """
    Retrieve a list of predefined loop tags for
    atomic site description.
    """
    loop_tags = get_loop_tags()

    loop_values = [block.find_loop(tag) for tag in loop_tags]

    return loop_values


def get_unique_label_count(loop_values: list) -> int:
    """
    Count the number of labels in the loop.
    """
    return len(loop_values[0])


def get_unique_elements_from_loop(loop_values: list) -> set[str]:
    """
    Return a list of unique elements from loop values.
    """
    num_atom_labels = get_unique_label_count(loop_values)
    element_list = []
    for i in range(num_atom_labels):
        element = loop_values[1][i]
        element_list.append(str(element))
    return set(element_list)


def get_unique_site_labels(loop_values: list) -> list[str]:
    """
    Return a list of atom labels from loop values.
    """
    num_atom_labels = get_unique_label_count(loop_values)
    label_list = []
    for i in range(num_atom_labels):
        element = loop_values[0][i]
        label_list.append(element)

    return label_list


def get_label_occupancy_coordinates(
    loop_values: list, i
) -> tuple[str, float, tuple[float, float, float]]:
    """
    Return atom information (label, occupancy, coordinates) for the i-th atom.
    """
    label: str = loop_values[0][i]
    occupancy: float = get_string_to_formatted_float(loop_values[7][i])
    coordinates: tuple[float, float, float] = (
        get_string_to_formatted_float(loop_values[4][i]),
        get_string_to_formatted_float(loop_values[5][i]),
        get_string_to_formatted_float(loop_values[6][i]),
    )

    return label, occupancy, coordinates


def get_loop_value_dict(
    loop_values: list,
) -> dict[str, dict[str, Any]]:
    """
    Create a dictionary containing CIF loop values for each label.
    """
    loop_value_dict = {}
    num_of_atom_labels = get_unique_label_count(loop_values)

    for i in range(num_of_atom_labels):
        label, occupancy, coordinates = get_label_occupancy_coordinates(
            loop_values, i
        )
        loop_value_dict[label] = {
            "occupancy": occupancy,
            "coords": coordinates,
        }

    return loop_value_dict


def get_start_end_line_indexes(
    file_path: str, start_keyword: str
) -> tuple[int, int]:
    """
    Find the starting and ending indexes of the lines in atom_site_loop
    """

    with open(file_path, "r") as f:
        lines = f.readlines()

    start_index = 0
    end_index = 0

    # Find the start index
    for i, line in enumerate(lines):
        if start_keyword in line:
            start_index = i + 1
            break

    # Find the end index
    for i in range(start_index, len(lines)):
        if lines[i].strip() == "":
            end_index = i
            break

    return start_index, end_index


def get_line_content_from_tag(file_path: str, start_keyword: str) -> list[str]:
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


def get_formula_structure_weight_s_group(
    block: Block,
) -> tuple[str, str, float, int, str]:
    """
    Return the unit cell lengths.
    """
    keys = [
        "_chemical_formula_structural",
        "_chemical_name_structure_type",
        "_chemical_formula_weight",
        "_space_group_IT_number",
        "_space_group_name_H-M_alt",
    ]

    values = [(block.find_value(key)) for key in keys]

    formula = trim_string(values[0])
    structure = clean_parsed_structure(values[1])
    weight = get_string_to_formatted_float(values[2])
    s_group_num = int(trim_string(values[3]))
    s_group_name = trim_string(values[4])

    return (formula, structure, weight, s_group_num, s_group_name)


def get_unique_formulas_structures_weights_s_groups(
    file_path_list: list[str],
) -> tuple[set[str], set[str], set[float], set[int], set[str]]:
    """
    Find all unique structures, formulas, weights, space groups.
    This function requires no initialization and should be more efficient
    in analyzing and filtering a dataset.
    """
    formulas = set()
    structures = set()
    weights = set()
    s_group_nums = set()
    s_group_names = set()
    for file_path in file_path_list:
        block = get_cif_block(file_path)
        formula, structure, weight, s_group_num, s_group_name = (
            get_formula_structure_weight_s_group(block)
        )

        formulas.add(formula)
        structures.add(structure)
        weights.add(weight)
        s_group_nums.add(s_group_num)
        s_group_names.add(s_group_name)

    return formulas, structures, weights, s_group_nums, s_group_names


def get_tag_from_third_line(file_path: str) -> str:
    """
    Extract the tag from the provided CIF file path.
    """
    with open(file_path, "r") as f:
        # Read first three lines
        f.readline()  # First line
        f.readline()  # Second line
        third_line = f.readline().strip()  # Thrid line
        third_line = third_line.replace(",", "")

        # Split based on '#' and filter out empty strings
        third_line_parts = [
            part.strip() for part in third_line.split("#") if part.strip()
        ]

        formula_tag = third_line_parts[1]
        parts = formula_tag.split()

        # Return concatenated string of parts excluding the first one
        if len(parts) > 1:
            return "_".join(parts[1:])
        else:
            return ""


def parse_atom_site_occupancy_info(file_path: str) -> dict:
    """Parse atom site loop information including element, occupancy,
    fractional coordinates, multiplicity, and wyckoff symbol."""
    content_lines = get_line_content_from_tag(
        file_path, "_atom_site_occupancy"
    )

    parsed_data = {}

    for line in content_lines:
        parts = line.split()
        atom_site_label = parts[0]
        element = parts[1]
        symmetry_multiplicity = int(parts[2])
        wyckoff_symbol = parts[3]
        x_frac_coord = float(parts[4])  # Fractional coordinate x
        y_frac_coord = float(parts[5])  # Fractional coordinate y
        z_frac_coord = float(parts[6])  # Fractional coordinate z
        site_occupancy = float(parts[7])

        parsed_data[atom_site_label] = {
            "element": element,
            "site_occupancy": site_occupancy,
            "x_frac_coord": x_frac_coord,  # Clearly label as fractional
            "y_frac_coord": y_frac_coord,  # Clearly label as fractional
            "z_frac_coord": z_frac_coord,  # Clearly label as fractional
            "symmetry_multiplicity": symmetry_multiplicity,
            "wyckoff_symbol": wyckoff_symbol,
        }

    return parsed_data


def check_unique_atom_site_labels(file_path: str):
    """Check whether all parsed atom site labels are unique."""
    content_lines = get_line_content_from_tag(
        file_path, "_atom_site_occupancy"
    )

    site_labels = set()
    for line in content_lines:
        parts = line.split()
        if len(parts) != 8:
            raise ValueError(CifParserError.WRONG_LOOP_VALUE_COUNT.value)

        parsed_site_label = parts[0]
        parsed_element = parts[1]
        site_labels.add(parsed_site_label)

        if get_atom_type_from_label(parsed_site_label) != parsed_element:
            raise ValueError(CifParserError.INVALID_PARSED_ELEMENT.value)

    # If the count of unique labels does not match the number of lines, raise an error
    if len(content_lines) != len(site_labels):
        raise ValueError(CifParserError.DUPLICATE_LABELS.value)