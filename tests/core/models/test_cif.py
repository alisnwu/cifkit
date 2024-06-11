import os, shutil
import pytest
from cifpy.utils.folder import get_file_path_list, make_output_folder
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


def test_cif_lazy_propertes_after_compute_connection(formula_URhIn, cif_URhIn):
    cif_URhIn.compute_connections()
    assert cif_URhIn.shortest_pair_distance == 2.697

    connections_CN = cif_URhIn.connections_CN
    assert len(connections_CN.get("In1")) == 14
    assert len(connections_CN.get("U1")) == 11
    assert len(connections_CN.get("Rh1")) == 9
    assert len(connections_CN.get("Rh2")) == 9

    expected_bond_counts = {
        "In1": {("In", "In"): 4, ("In", "Rh"): 4, ("In", "U"): 6},
        "Rh1": {("In", "Rh"): 3, ("Rh", "U"): 6},
        "Rh2": {("In", "Rh"): 6, ("Rh", "U"): 3},
        "U1": {("In", "U"): 6, ("Rh", "U"): 5},
    }
    assert cif_URhIn.bond_counts_CN == expected_bond_counts

    expected_shotest_pair_distance = {
        "In1": ("Rh2", 2.697),
        "Rh1": ("In1", 2.852),
        "Rh2": ("In1", 2.697),
        "U1": ("Rh1", 2.984),
    }
    result = cif_URhIn.shortest_distance_per_label

    assert all(
        result[label][0] == expected_shotest_pair_distance[label][0]
        and pytest.approx(result[label][1], 0.001)
        == expected_shotest_pair_distance[label][1]
        for label in expected_shotest_pair_distance
    )

    # Expected output based on input data
    expected_fractions = {
        ("In", "In"): 4 / 43,
        ("In", "Rh"): 13 / 43,
        ("In", "U"): 12 / 43,
        ("Rh", "U"): 14 / 43,
    }

    # Testing each bond fraction to ensure they are within a small tolerance
    for bond_type, expected_fraction in expected_fractions.items():
        assert (
            pytest.approx(cif_URhIn.bond_fraction_CN[bond_type], 0.005)
            == expected_fraction
        )

    # Testing to ensure the fractions sum approximately to 1
    assert pytest.approx(sum(cif_URhIn.bond_fraction_CN.values()), 0.005) == 1


def test_get_polyhedron_labels_from_site(cif_URhIn):

    expected_labels = [
        "Rh2",
        "Rh2",
        "Rh1",
        "Rh1",
        "U1",
        "U1",
        "In1",
        "In1",
        "U1",
        "U1",
        "U1",
        "U1",
        "In1",
        "In1",
        "In1",
    ]

    polyhedron_points, labels = cif_URhIn.get_polyhedron_labels_from_site(
        "In1"
    )
    assert len(polyhedron_points) == 15
    assert labels == expected_labels


def test_cif_lazy_propertes(cif_URhIn):
    assert cif_URhIn.shortest_pair_distance == 2.697

    connections_CN = cif_URhIn.connections_CN
    assert len(connections_CN.get("In1")) == 14
    assert len(connections_CN.get("U1")) == 11
    assert len(connections_CN.get("Rh1")) == 9
    assert len(connections_CN.get("Rh2")) == 9


"""Test polyhedron"""


def test_plot_polyhedron_default_output_folder(cif_URhIn):
    # Define the directory to store the output
    expected_output_dir = "tests/data/cif/polyhedrons"
    output_file_path = os.path.join(expected_output_dir, "URhIn_In1.png")

    # Ensure the directory exists
    if not os.path.exists(expected_output_dir):
        os.makedirs(expected_output_dir)

    # Define the output file path
    cif_URhIn.plot_polyhedron("In1")

    assert os.path.exists(output_file_path)
    assert os.path.getsize(output_file_path) > 1024
    shutil.rmtree(expected_output_dir)


def test_plot_polyhedron_with_output_folder_given(cif_URhIn):
    # Define the directory to store the output
    expected_output_dir = "tests/data/cif/polyhedrons_user"
    output_file_path = os.path.join(expected_output_dir, "URhIn_In1.png")

    # Ensure the directory exists
    if not os.path.exists(expected_output_dir):
        os.makedirs(expected_output_dir)

    # Define the output file path
    cif_URhIn.plot_polyhedron("In1", "tests/data/cif/polyhedrons_user")

    assert os.path.exists(output_file_path)
    assert os.path.getsize(output_file_path) > 1024
    shutil.rmtree(expected_output_dir)


"""Test error during init"""


def test_init_error_duplicate_label():
    file_path = "tests/data/cif/error/duplicate_labels/457848.cif"
    with pytest.raises(ValueError) as e:
        Cif(file_path)

    expected_error_message = CifParserError.DUPLICATE_LABELS.value
    assert expected_error_message == str(e.value)


def test_init_error_coord_missing():
    file_path = "tests/data/cif/error/missing_loop/452743.cif"
    with pytest.raises(ValueError) as e:
        Cif(file_path)
    expected_error_message = CifParserError.WRONG_LOOP_VALUE_COUNT.value
    assert expected_error_message == str(e.value)
