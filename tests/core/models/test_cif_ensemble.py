import pytest
from cifpy.models.cif_ensemble import CifEnsemble
from cifpy.utils.folder import get_file_count, get_file_path_list


@pytest.mark.fast
def test_init(cif_ensemble_test):
    # Create an instance of CifEnsemble
    assert cif_ensemble_test.cif_folder_path == "tests/data/cif/ensemble_test"
    assert cif_ensemble_test.unique_formulas == {
        "EuIr2Ge2",
        "CeRu2Ge2",
        "LaRu2Ge2",
        "Mo",
    }
    assert cif_ensemble_test.unique_structures == {"CeAl2Ga2", "W"}
    assert cif_ensemble_test.unique_elements == {
        "La",
        "Ru",
        "Ge",
        "Ir",
        "Eu",
        "Ce",
        "Mo",
    }
    assert cif_ensemble_test.unique_space_group_names == {
        "I4/mmm",
        "Im-3m",
    }
    assert cif_ensemble_test.unique_space_group_numbers == {139, 229}
    assert cif_ensemble_test.unique_tags == {"hex", "rt", "rt_hex", ""}

    assert cif_ensemble_test.minimum_distances == [
        ("tests/data/cif/ensemble_test/300169.cif", 2.29),
        ("tests/data/cif/ensemble_test/260171.cif", 2.72),
        ("tests/data/cif/ensemble_test/250697.cif", 2.725),
        ("tests/data/cif/ensemble_test/250709.cif", 2.725),
        ("tests/data/cif/ensemble_test/300171.cif", 2.383),
        ("tests/data/cif/ensemble_test/300170.cif", 2.28),
    ]

    assert cif_ensemble_test.supercell_atom_counts == [
        ("tests/data/cif/ensemble_test/300169.cif", 360),
        ("tests/data/cif/ensemble_test/260171.cif", 54),
        ("tests/data/cif/ensemble_test/250697.cif", 54),
        ("tests/data/cif/ensemble_test/250709.cif", 54),
        ("tests/data/cif/ensemble_test/300171.cif", 360),
        ("tests/data/cif/ensemble_test/300170.cif", 360),
    ]


@pytest.mark.fast
def test_filter_files(cif_ensemble_test):
    cif_ensemble_test = CifEnsemble("tests/data/cif/ensemble_test")

    # Test filter by specific formula
    assert cif_ensemble_test.filter_by_formulas(["LaRu2Ge2"]) == {
        "tests/data/cif/ensemble_test/300169.cif",
    }

    assert cif_ensemble_test.filter_by_formulas(["LaRu2Ge2", "Mo"]) == {
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/260171.cif",
        "tests/data/cif/ensemble_test/250697.cif",
        "tests/data/cif/ensemble_test/250709.cif",
    }

    # Test filter by structure
    assert cif_ensemble_test.filter_by_structures(["W"]) == {
        "tests/data/cif/ensemble_test/260171.cif",
        "tests/data/cif/ensemble_test/250697.cif",
        "tests/data/cif/ensemble_test/250709.cif",
    }

    assert cif_ensemble_test.filter_by_structures("CeAl2Ga2") == {
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/300171.cif",
        "tests/data/cif/ensemble_test/300170.cif",
    }

    assert cif_ensemble_test.filter_by_elements(["La"]) == {
        "tests/data/cif/ensemble_test/300169.cif",
    }

    assert cif_ensemble_test.filter_by_elements(["Ge"]) == {
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/300171.cif",
        "tests/data/cif/ensemble_test/300170.cif",
    }

    assert cif_ensemble_test.filter_by_elements(["Ge", "Ru"]) == {
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/300170.cif",
    }

    # Test filter by space group
    assert cif_ensemble_test.filter_by_space_group_names("Im-3m") == {
        "tests/data/cif/ensemble_test/260171.cif",
        "tests/data/cif/ensemble_test/250697.cif",
        "tests/data/cif/ensemble_test/250709.cif",
    }

    assert cif_ensemble_test.filter_by_space_group_numbers([139]) == {
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/300171.cif",
        "tests/data/cif/ensemble_test/300170.cif",
    }


@pytest.mark.fast
def test_move_files(tmp_path, cif_ensemble_test):
    file_paths = {
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/300171.cif",
        "tests/data/cif/ensemble_test/300170.cif",
    }
    dest_dir = tmp_path / "destination"
    initial_dir_path = "tests/data/cif/ensemble_test"
    initial_file_count = get_file_count(initial_dir_path)
    # Move files to the destination directory
    cif_ensemble_test.move_cif_files(file_paths, dest_dir)
    assert get_file_count(dest_dir) == initial_file_count - len(file_paths)
    cif_ensemble_test.move_cif_files(
        set(get_file_path_list(dest_dir)), initial_dir_path
    )
    assert get_file_count(initial_dir_path) == initial_file_count


@pytest.mark.fast
def test_copy_files(tmp_path, cif_ensemble_test):
    file_paths = {
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/300171.cif",
        "tests/data/cif/ensemble_test/300170.cif",
    }
    dest_dir = tmp_path / "destination"
    # Move files to the destination directory
    cif_ensemble_test.copy_cif_files(file_paths, dest_dir)
    assert get_file_count(dest_dir) == len(file_paths)
