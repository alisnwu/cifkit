import pytest
from cifpy.utils.folder import get_file_path_list
from cifpy.models.cif import Cif
from cifpy.utils.error_messages import CifParserError


def test_cif_static_properties(cif_URhIn):
    assert cif_URhIn.unique_elements == {"U", "In", "Rh"}
    assert cif_URhIn.formula == "URhIn"
    assert cif_URhIn.structure == "ZrNiAl"
    assert cif_URhIn.site_labels == ["In1", "U1", "Rh1", "Rh2"]
    assert cif_URhIn.space_group_name == "P-62m"
    assert cif_URhIn.space_group_number == 189
    assert cif_URhIn.tag == "rt"
    assert cif_URhIn.heterogeneous_bond_pairs == {
        ("In", "Rh"),
        ("In", "U"),
        ("Rh", "U"),
    }
    assert cif_URhIn.homogenous_bond_pairs == {
        ("U", "U"),
        ("Rh", "Rh"),
        ("In", "In"),
    }

    assert cif_URhIn.all_bond_pairs == {
        ("U", "U"),
        ("Rh", "Rh"),
        ("In", "In"),
        ("In", "Rh"),
        ("In", "U"),
        ("Rh", "U"),
    }

    assert cif_URhIn.atom_site_info == {
        "In1": {
            "element": "In",
            "site_occupancy": 1.0,
            "x_frac_coord": 0.2505,
            "y_frac_coord": 0.0,
            "z_frac_coord": 0.5,
            "symmetry_multiplicity": 3,
            "wyckoff_symbol": "g",
        },
        "U1": {
            "element": "U",
            "site_occupancy": 1.0,
            "x_frac_coord": 0.5925,
            "y_frac_coord": 0.0,
            "z_frac_coord": 0.0,
            "symmetry_multiplicity": 3,
            "wyckoff_symbol": "f",
        },
        "Rh1": {
            "element": "Rh",
            "site_occupancy": 1.0,
            "x_frac_coord": 0.333333,
            "y_frac_coord": 0.666667,
            "z_frac_coord": 0.5,
            "symmetry_multiplicity": 2,
            "wyckoff_symbol": "d",
        },
        "Rh2": {
            "element": "Rh",
            "site_occupancy": 1.0,
            "x_frac_coord": 0.0,
            "y_frac_coord": 0.0,
            "z_frac_coord": 0.0,
            "symmetry_multiplicity": 1,
            "wyckoff_symbol": "a",
        },
    }


def test_cif_lazy_propertes_after_compute_connection(cif_URhIn):
    cif_URhIn.compute_connections()
    assert cif_URhIn.shortest_pair_distance == 2.697

    connections_CN = cif_URhIn.connections_CN
    assert len(connections_CN.get("In1")) == 14
    assert len(connections_CN.get("U1")) == 11
    assert len(connections_CN.get("Rh1")) == 9
    assert len(connections_CN.get("Rh2")) == 9


def test_cif_lazy_propertes(cif_URhIn):
    assert cif_URhIn.shortest_pair_distance == 2.697

    connections_CN = cif_URhIn.connections_CN
    assert len(connections_CN.get("In1")) == 14
    assert len(connections_CN.get("U1")) == 11
    assert len(connections_CN.get("Rh1")) == 9
    assert len(connections_CN.get("Rh2")) == 9


"""Test error during init"""


def test_init_error_duplicate_label():
    file_path = "tests/data/cif/error/duplicate_labels/457848.cif"
    with pytest.raises(ValueError) as e:
        Cif(file_path)

    expected_error_message = CifParserError.DUPLICATE_LABELS.value
    assert expected_error_message == str(e.value)


@pytest.mark.fast
def test_init_error_coord_missing():
    file_path = "tests/data/cif/error/missing_loop/452743.cif"
    with pytest.raises(ValueError) as e:
        Cif(file_path)
    expected_error_message = CifParserError.WRONG_LOOP_VALUE_COUNT.value
    assert expected_error_message == str(e.value)


def test_init_error_label():
    """
    A,C Fe 8 c 0.25 0.25 0.25 1
    Fe Fe 4 b 0.5 0.5 0.5 1
    Si Si 4 a 0 0 0 1
    """
    file_path = "tests/data/cif/error/error_label/1819643.cif"
    with pytest.raises(ValueError) as e:
        Cif(file_path)
    expected_error_message = CifParserError.INVALID_PARSED_ELEMENT.value
    assert expected_error_message == str(e.value)
