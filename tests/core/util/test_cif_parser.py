import pytest

from cifpy.utils.error_messages import GeneralError, CifParserError
from cifpy.utils import folder
from cifpy.utils.cif_parser import (
    get_cif_block,
    get_unitcell_lengths,
    get_unitcell_angles_rad,
    get_loop_tags,
    get_loop_values,
    get_unique_label_count,
    get_unique_elements_from_loop,
    get_unique_site_labels,
    get_label_occupancy_coordinates,
    get_loop_value_dict,
    get_start_end_line_indexes,
    get_line_content_from_tag,
    get_formula_structure_weight_s_group,
    get_unique_formulas_structures_weights_s_groups,
    get_tag_from_third_line,
)


def test_get_cif_block(cif_block_URhIn):
    assert cif_block_URhIn is not None


def test_get_unit_cell_lengths_angles(cif_block_URhIn):
    lengths = get_unitcell_lengths(cif_block_URhIn)
    angles = get_unitcell_angles_rad(cif_block_URhIn)

    assert lengths == [7.476, 7.476, 3.881]
    assert angles == [1.5708, 1.5708, 2.0944]


def test_get_loop_tags():
    expected_tags = [
        "_atom_site_label",
        "_atom_site_type_symbol",
        "_atom_site_symmetry_multiplicity",
        "_atom_site_Wyckoff_symbol",
        "_atom_site_fract_x",
        "_atom_site_fract_y",
        "_atom_site_fract_z",
        "_atom_site_occupancy",
    ]

    assert (
        get_loop_tags() == expected_tags
    ), CifParserError.INVALID_LOOP_TAGS.value


def test_get_loop_values(cif_block_URhIn):
    loop_values = get_loop_values(cif_block_URhIn)

    assert loop_values[0][0] == "In1"
    assert loop_values[0][1] == "U1"
    assert loop_values[0][2] == "Rh1"
    assert loop_values[0][3] == "Rh2"
    assert loop_values[1][0] == "In"
    assert loop_values[1][1] == "U"
    assert loop_values[1][2] == "Rh"
    assert loop_values[1][3] == "Rh"


def test_get_loop_values_wrong_loop_number():
    file_path = "tests/data/cif/URhIn_bad_loop_format.cif"
    with pytest.raises(ValueError) as e:
        get_cif_block(file_path)
    assert CifParserError.WRONG_LOOP_VALUE.value in str(e.value)


def test_get_num_of_atom_unique_labels(loop_values_URhIn):
    assert get_unique_label_count(loop_values_URhIn) == 4


def test_get_unique_elements(loop_values_URhIn):
    assert get_unique_elements_from_loop(loop_values_URhIn) == {
        "In",
        "Rh",
        "U",
    }


def test_get_atom_labels(loop_values_URhIn):
    assert get_unique_site_labels(loop_values_URhIn) == [
        "In1",
        "U1",
        "Rh1",
        "Rh2",
    ]


def test_get_label_occupancy_coordinates(loop_values_URhIn):
    label, occupacny, coordinates = get_label_occupancy_coordinates(
        loop_values_URhIn, 0
    )
    assert label == "In1"
    assert occupacny == 1.0
    assert coordinates == (0.2505, 0.0, 0.5)

    label, occupacny, coordinates = get_label_occupancy_coordinates(
        loop_values_URhIn, 1
    )
    assert label == "U1"
    assert occupacny == 1.0
    assert coordinates == (0.5925, 0.0, 0.0)


def test_get_loop_value_dict(loop_values_URhIn):
    expected_dict = {
        "In1": {"coords": (0.2505, 0.0, 0.5), "occupancy": 1.0},
        "Rh1": {
            "coords": (0.333333, 0.666667, 0.5),
            "occupancy": 1.0,
        },
        "Rh2": {"coords": (0.0, 0.0, 0.0), "occupancy": 1.0},
        "U1": {"coords": (0.5925, 0.0, 0.0), "occupancy": 1.0},
    }

    assert get_loop_value_dict(loop_values_URhIn) == expected_dict


def test_get_start_end_line_indexes():
    file_path = "tests/data/cif/author.cif"
    keyword = "_publ_author_address"
    # Line 54-103 before space a provided
    assert get_start_end_line_indexes(file_path, keyword) == (
        54,
        103,
    )


def test_get_line_content_from_tag(file_path_URhIn):
    content_lines = get_line_content_from_tag(
        file_path_URhIn, "_atom_site_occupancy"
    )

    assert len(content_lines) == 4
    assert content_lines[0].strip() == "In1 In 3 g 0.2505 0 0.5 1"
    assert content_lines[1].strip() == "U1 U 3 f 0.5925 0 0 1"
    assert content_lines[2].strip() == "Rh1 Rh 2 d 0.333333 0.666667 0.5 1"
    assert content_lines[3].strip() == "Rh2 Rh 1 a 0 0 0 1"


def test_get_formula_structure_weight_sgroup(cif_block_URhIn):
    parsed_result = get_formula_structure_weight_s_group(cif_block_URhIn)
    formula, structure, weight, s_group_num, s_group_name = parsed_result
    assert formula == "URhIn"
    assert structure == "ZrNiAl"
    assert weight == 455.8
    assert s_group_num == 189
    assert s_group_name == "P-62m"


def test_get_unique_formulas_structure_weight(cif_folder_path_test):
    file_path_list = folder.get_file_path_list(cif_folder_path_test)
    formulas, structures, weights, s_group_nums, s_group_names = (
        get_unique_formulas_structures_weights_s_groups(file_path_list)
    )
    assert formulas == {"LaRu2Ge2", "CeRu2Ge2", "EuIr2Ge2"}
    assert structures == {"CeAl2Ga2"}
    assert weights == {486.2, 487.4, 681.6}
    assert s_group_nums == {139}
    assert s_group_names == {"I4/mmm"}


def test_get_tag_from_third_line():
    file_path = "tests/data/cif/tag/1817275_rt.cif"
    assert get_tag_from_third_line(file_path) == "rt"

    file_path = "tests/data/cif/tag/1817275_rt_hex.cif"
    assert get_tag_from_third_line(file_path) == "rt_hex"
