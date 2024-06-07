import pytest
from cifpy.models.cif_ensemble import CifEnsemble


@pytest.mark.fast
def test_init():
    # Create an instance of CifEnsemble
    cif_ensemble = CifEnsemble("tests/data/cif/ensemble_test")
    assert cif_ensemble.cif_folder_path == "tests/data/cif/ensemble_test"

    # Fetch unique values from the ensemble
    unique_formulas = cif_ensemble.get_unique_formulas()
    unique_structures = cif_ensemble.get_unique_structures()
    unique_elements = cif_ensemble.get_unique_elements()
    unique_space_group_names = cif_ensemble.get_unique_space_group_names()
    unique_space_group_numbers = cif_ensemble.get_unique_space_group_numbers()

    # Print these values (optional, typically not done in unit tests)
    print("Unique Formulas:", unique_formulas)
    print("Unique Structures:", unique_structures)
    print("Unique Elements:", unique_elements)
    print("Unique Space Group Names:", unique_space_group_names)
    print("Unique Space Group Numbers:", unique_space_group_numbers)

    # Assert that the fetched values are as expected
    assert unique_formulas == {"EuIr2Ge2", "CeRu2Ge2", "LaRu2Ge2", "Mo"}
    assert unique_structures == {"CeAl2Ga2", "W"}
    assert unique_elements == {"La", "Ru", "Ge", "Ir", "Eu", "Ce", "Mo"}
    assert unique_space_group_names == {"I4/mmm", "Im-3m"}
    assert unique_space_group_numbers == {139, 229}
    # assert False


@pytest.mark.fast
def test_filter():
    cif_ensemble = CifEnsemble("tests/data/cif/ensemble_test")

    # Test filter by specific formula
    assert cif_ensemble.filter_by_formula("Mo") == [
        "tests/data/cif/ensemble_test/260171.cif",
        "tests/data/cif/ensemble_test/250697.cif",
        "tests/data/cif/ensemble_test/250709.cif",
    ]
    assert cif_ensemble.filter_by_formula("LaRu2Ge2") == [
        "tests/data/cif/ensemble_test/300169.cif",
    ]

    # Test filter by structure
    assert cif_ensemble.filter_by_structure("W") == [
        "tests/data/cif/ensemble_test/260171.cif",
        "tests/data/cif/ensemble_test/250697.cif",
        "tests/data/cif/ensemble_test/250709.cif",
    ]

    assert cif_ensemble.filter_by_structure("CeAl2Ga2") == [
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/300171.cif",
        "tests/data/cif/ensemble_test/300170.cif",
    ]

    assert cif_ensemble.filter_by_elements(["La"]) == [
        "tests/data/cif/ensemble_test/300169.cif",
    ]
    assert cif_ensemble.filter_by_elements(["Ge"]) == [
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/300171.cif",
        "tests/data/cif/ensemble_test/300170.cif",
    ]

    assert cif_ensemble.filter_by_elements(["Ge", "Ru"]) == [
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/300170.cif",
    ]

    # Test filter by space group
    assert cif_ensemble.filter_by_space_group_name("Im-3m") == [
        "tests/data/cif/ensemble_test/260171.cif",
        "tests/data/cif/ensemble_test/250697.cif",
        "tests/data/cif/ensemble_test/250709.cif",
    ]

    assert cif_ensemble.filter_by_space_group_number(139) == [
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/300171.cif",
        "tests/data/cif/ensemble_test/300170.cif",
    ]
