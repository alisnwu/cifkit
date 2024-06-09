import pytest
from cifpy.models.cif_ensemble import CifEnsemble


@pytest.mark.fast
def test_init():
    # Create an instance of CifEnsemble
    cif_ensemble = CifEnsemble("tests/data/cif/ensemble_test")
    assert cif_ensemble.cif_folder_path == "tests/data/cif/ensemble_test"
    assert cif_ensemble.unique_formulas == {
        "EuIr2Ge2",
        "CeRu2Ge2",
        "LaRu2Ge2",
        "Mo",
    }
    assert cif_ensemble.unique_structures == {"CeAl2Ga2", "W"}
    assert cif_ensemble.unique_elements == {
        "La",
        "Ru",
        "Ge",
        "Ir",
        "Eu",
        "Ce",
        "Mo",
    }
    assert cif_ensemble.unique_space_group_names == {
        "I4/mmm",
        "Im-3m",
    }
    assert cif_ensemble.unique_space_group_numbers == {139, 229}
    assert cif_ensemble.unique_tags == {"hex", "rt", "rt_hex", ""}

    assert cif_ensemble.minimum_distances == [
        ("tests/data/cif/ensemble_test/300169.cif", 2.29),
        ("tests/data/cif/ensemble_test/260171.cif", 2.72),
        ("tests/data/cif/ensemble_test/250697.cif", 2.725),
        ("tests/data/cif/ensemble_test/250709.cif", 2.725),
        ("tests/data/cif/ensemble_test/300171.cif", 2.383),
        ("tests/data/cif/ensemble_test/300170.cif", 2.28),
    ]

    assert cif_ensemble.supercell_atom_counts == [
        ("tests/data/cif/ensemble_test/300169.cif", 360),
        ("tests/data/cif/ensemble_test/260171.cif", 54),
        ("tests/data/cif/ensemble_test/250697.cif", 54),
        ("tests/data/cif/ensemble_test/250709.cif", 54),
        ("tests/data/cif/ensemble_test/300171.cif", 360),
        ("tests/data/cif/ensemble_test/300170.cif", 360),
    ]


@pytest.mark.fast
def test_filter():
    cif_ensemble = CifEnsemble("tests/data/cif/ensemble_test")

    # Test filter by specific formula
    assert cif_ensemble.filter_by_formulas(["LaRu2Ge2"]) == {
        "tests/data/cif/ensemble_test/300169.cif",
    }

    assert cif_ensemble.filter_by_formulas(["LaRu2Ge2", "Mo"]) == {
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/260171.cif",
        "tests/data/cif/ensemble_test/250697.cif",
        "tests/data/cif/ensemble_test/250709.cif",
    }

    # Test filter by structure
    assert cif_ensemble.filter_by_structures(["W"]) == {
        "tests/data/cif/ensemble_test/260171.cif",
        "tests/data/cif/ensemble_test/250697.cif",
        "tests/data/cif/ensemble_test/250709.cif",
    }

    assert cif_ensemble.filter_by_structures("CeAl2Ga2") == {
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/300171.cif",
        "tests/data/cif/ensemble_test/300170.cif",
    }

    assert cif_ensemble.filter_by_elements(["La"]) == {
        "tests/data/cif/ensemble_test/300169.cif",
    }

    assert cif_ensemble.filter_by_elements(["Ge"]) == {
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/300171.cif",
        "tests/data/cif/ensemble_test/300170.cif",
    }

    assert cif_ensemble.filter_by_elements(["Ge", "Ru"]) == {
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/300170.cif",
    }

    # Test filter by space group
    assert cif_ensemble.filter_by_space_group_names("Im-3m") == {
        "tests/data/cif/ensemble_test/260171.cif",
        "tests/data/cif/ensemble_test/250697.cif",
        "tests/data/cif/ensemble_test/250709.cif",
    }

    assert cif_ensemble.filter_by_space_group_numbers([139]) == {
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/300171.cif",
        "tests/data/cif/ensemble_test/300170.cif",
    }
