import pytest
from cifpy.models.cif_ensemble import CifEnsemble
from cifpy.utils.folder import get_file_count, get_file_path_list


def test_init(cif_ensemble_test):
    # Create an instance of CifEnsemble
    assert cif_ensemble_test.dir_path == "tests/data/cif/ensemble_test"
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


"""
Test filter by value
"""


def test_filter_by_value(cif_ensemble_test):
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


"""
Test filter by range
"""


def test_filter_by_supercell_count(cif_ensemble_test):
    result = cif_ensemble_test.filter_by_supercell_count(200, 400)
    expected = {
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/300171.cif",
        "tests/data/cif/ensemble_test/300170.cif",
    }
    assert result == expected

    result = cif_ensemble_test.filter_by_supercell_count(50, 60)
    expected = {
        "tests/data/cif/ensemble_test/260171.cif",
        "tests/data/cif/ensemble_test/250697.cif",
        "tests/data/cif/ensemble_test/250709.cif",
    }
    assert result == expected


def test_filter_by_min_distance(cif_ensemble_test):
    result = cif_ensemble_test.filter_by_min_distance(2.0, 2.5)
    expected = {
        "tests/data/cif/ensemble_test/300171.cif",
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/300170.cif",
    }
    assert result == expected


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


"""
Test stats
"""


def test_structures_stats(cif_ensemble_test):
    result = cif_ensemble_test.structures_stats
    expected = {"CeAl2Ga2": 3, "W": 3}
    assert result == expected


def test_formula_stats(cif_ensemble_test):
    result = cif_ensemble_test.formula_stats
    expected = {"CeRu2Ge2": 1, "EuIr2Ge2": 1, "LaRu2Ge2": 1, "Mo": 3}
    assert result == expected


def test_tag_stats(cif_ensemble_test):
    result = cif_ensemble_test.tag_stats
    expected = {"": 2, "hex": 1, "rt": 2, "rt_hex": 1}
    assert result == expected


def test_space_group_number_stats(cif_ensemble_test):
    result = cif_ensemble_test.space_group_number_stats
    expected = {139: 3, 229: 3}
    assert result == expected


def test_space_group_name_stats(cif_ensemble_test):
    result = cif_ensemble_test.space_group_name_stats
    expected = {"I4/mmm": 3, "Im-3m": 3}
    assert result == expected


def test_supercell_size_stats(cif_ensemble_test):
    result = cif_ensemble_test.supercell_size_stats
    expected = {54: 3, 360: 3}
    assert result == expected


def test_min_distance_stats(cif_ensemble_test):
    result = cif_ensemble_test.min_distance_stats
    expected = {2.28: 1, 2.29: 1, 2.383: 1, 2.725: 2, 2.72: 1}
    assert result == expected


def test_unique_elements_stats(cif_ensemble_test):
    result = cif_ensemble_test.unique_elements_stats
    expected = {"Ce": 1, "Eu": 1, "Ge": 3, "Ir": 1, "La": 1, "Mo": 3, "Ru": 2}
    assert result == expected


"""
Test stat histograms
"""


def test_generate_histogram(cif_ensemble_test, tmp_path):
    output_dir = tmp_path / "histograms"
    cif_ensemble_test.generate_stat_histograms(output_dir=str(output_dir))

    # List of expected files
    expected_files = [
        "structures.png",
        "formula.png",
        "tag.png",
        "space_group_number.png",
        "space_group_name.png",
        "supercell_size.png",
        "min_distance.png",
        "unique_elements.png",
    ]

    # Check that all expected files are created
    for file_name in expected_files:
        file_path = output_dir / file_name
        assert file_path.exists()
