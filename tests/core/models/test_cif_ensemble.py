from pathlib import Path
import pytest
from cifkit import CifEnsemble
from cifkit.utils.folder import get_file_count, get_file_paths


@pytest.mark.fast
def test_init(cif_ensemble_test: CifEnsemble):
    assert cif_ensemble_test.dir_path == "tests/data/cif/ensemble_test"
    assert cif_ensemble_test.file_count == 6


def test_unique_values(cif_ensemble_test: CifEnsemble):
    assert cif_ensemble_test.unique_formulas == {
        "EuIr2Ge2",
        "CeRu2Ge2",
        "LaRu2Ge2",
        "Mo",
    }
    assert cif_ensemble_test.unique_structures == {"CeAl2Ga2", "W"}
    assert cif_ensemble_test.unique_space_group_names == {
        "I4/mmm",
        "Im-3m",
    }
    assert cif_ensemble_test.unique_space_group_numbers == {139, 229}
    assert cif_ensemble_test.unique_composition_types == {1, 3}
    assert cif_ensemble_test.unique_tags == {
        "hex",
        "rt",
        "rt_hex",
        "",
    }

    assert cif_ensemble_test.unique_site_mixing_types == {
        "deficiency_without_atomic_mixing",
        "full_occupancy",
    }

    # Test from a set
    # assert cif_ensemble_test.unique_coordination_numbers == {5, 9, 12, 14, 16}
    assert cif_ensemble_test.unique_elements == {
        "La",
        "Ru",
        "Ge",
        "Ir",
        "Eu",
        "Ce",
        "Mo",
    }


@pytest.mark.fast
def test_distances_supercell_size(cif_ensemble_test: CifEnsemble):
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


def test_filter_by_value(cif_ensemble_test: CifEnsemble):
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

    assert cif_ensemble_test.filter_by_structures(["CeAl2Ga2"]) == {
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/300171.cif",
        "tests/data/cif/ensemble_test/300170.cif",
    }

    # Test filter by space group
    assert cif_ensemble_test.filter_by_space_group_names(["Im-3m"]) == {
        "tests/data/cif/ensemble_test/260171.cif",
        "tests/data/cif/ensemble_test/250697.cif",
        "tests/data/cif/ensemble_test/250709.cif",
    }

    assert cif_ensemble_test.filter_by_space_group_numbers([139]) == {
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/300171.cif",
        "tests/data/cif/ensemble_test/300170.cif",
    }

    # Site mixing types
    assert cif_ensemble_test.filter_by_site_mixing_types(["full_occupancy"]) == {
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/300170.cif",
        "tests/data/cif/ensemble_test/260171.cif",
        "tests/data/cif/ensemble_test/250697.cif",
        "tests/data/cif/ensemble_test/250709.cif",
    }

    assert cif_ensemble_test.filter_by_site_mixing_types(
        ["deficiency_without_atomic_mixing"]
    ) == {
        "tests/data/cif/ensemble_test/300171.cif",
    }

    assert cif_ensemble_test.filter_by_site_mixing_types(
        ["full_occupancy", "deficiency_without_atomic_mixing"]
    ) == {
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/300170.cif",
        "tests/data/cif/ensemble_test/260171.cif",
        "tests/data/cif/ensemble_test/250697.cif",
        "tests/data/cif/ensemble_test/250709.cif",
        "tests/data/cif/ensemble_test/300171.cif",
    }

    assert cif_ensemble_test.filter_by_composition_types([3]) == {
        "tests/data/cif/ensemble_test/300171.cif",
        "tests/data/cif/ensemble_test/300170.cif",
        "tests/data/cif/ensemble_test/300169.cif",
    }


"""
Filter by set
Type 1. Element
"""


@pytest.mark.fast
def test_filter_by_elements(cif_ensemble_test):
    assert cif_ensemble_test.filter_by_elements_containing(["Ge"]) == {
        "tests/data/cif/ensemble_test/300171.cif",
        "tests/data/cif/ensemble_test/300170.cif",
        "tests/data/cif/ensemble_test/300169.cif",
    }

    assert cif_ensemble_test.filter_by_elements_exact_matching(["Ge", "Ru", "La"]) == {
        "tests/data/cif/ensemble_test/300169.cif",
    }


"""
Filter by set
Type 2. Coordination numbers
"""


@pytest.mark.fast
def test_filter_by_CN_dist_method_containing(
    cif_ensemble_test: CifEnsemble,
):
    # cif_ensemble_test.CN_unique_values_by_min_dist_method)
    # {16, 5, 9, 12, 14}
    # cif_ensemble_test.CN_unique_values_by_best_methods)
    # {16, 9, 10, 12, 14}
    # "tests/data/cif/ensemble_test/300170.cif" - best methods
    # {16, 10, 12}
    # "tests/data/cif/ensemble_test/300170.cif" - min dist method
    # {16, 12, 5}

    assert cif_ensemble_test.filter_by_CN_dist_method_containing([5]) == {
        "tests/data/cif/ensemble_test/300170.cif",
        "tests/data/cif/ensemble_test/300169.cif",
    }


@pytest.mark.fast
def test_filter_by_CN_dist_method_exact_matching(
    cif_ensemble_test: CifEnsemble,
):
    assert cif_ensemble_test.filter_by_CN_dist_method_exact_matching([14]) == {
        "tests/data/cif/ensemble_test/260171.cif",
        "tests/data/cif/ensemble_test/250709.cif",
        "tests/data/cif/ensemble_test/250697.cif",
    }


@pytest.mark.fast
def test_filter_by_CN_best_methods_containing(
    cif_ensemble_test: CifEnsemble,
):
    assert cif_ensemble_test.filter_by_CN_best_methods_containing([5]) == set()
    assert cif_ensemble_test.filter_by_CN_best_methods_containing([10]) == {
        "tests/data/cif/ensemble_test/300170.cif",
        "tests/data/cif/ensemble_test/300169.cif",
    }


@pytest.mark.fast
def test_filter_by_CN_best_methods_exact_matching(
    cif_ensemble_test: CifEnsemble,
):
    assert cif_ensemble_test.filter_by_CN_best_methods_exact_matching([10]) == set()


"""#
tests/data/cif/ensemble_test/300169.cif
{'Ge1': 5, 'Ru1': 12, 'La1': 16}
tests/data/cif/ensemble_test/260171.cif
{'Mo': 14}
tests/data/cif/ensemble_test/250697.cif
{'Mo': 14}
tests/data/cif/ensemble_test/250709.cif
{'Mo': 14}
tests/data/cif/ensemble_test/300171.cif
{'Ge1': 9, 'Ir1': 12, 'Eu1': 16}
tests/data/cif/ensemble_test/300170.cif
{'Ge1': 5, 'Ru1': 12, 'Ce1': 16}
"""


"""
Test filter by value
"""


# assert cif_ensemble_test.filter_by_CN_min_dist_method_exact_matching(
#     [16]
# ) == {
#     "tests/data/cif/ensemble_test/300169.cif",
#     "tests/data/cif/ensemble_test/300170.cif",
#     "tests/data/cif/ensemble_test/300171.cif",
# }

# assert cif_ensemble_test.filter_by_CN_min_dist_method_exact_matching(
#     [9, 12, 16]
# ) == {
#     "tests/data/cif/ensemble_test/300171.cif",
# }


# """
# Test filter by rang
# """


@pytest.mark.fast
def test_filter_by_supercell_count(cif_ensemble_test: CifEnsemble):
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


@pytest.mark.fast
def test_filter_by_min_distance(cif_ensemble_test: CifEnsemble):
    result = cif_ensemble_test.filter_by_min_distance(2.0, 2.5)
    expected = {
        "tests/data/cif/ensemble_test/300171.cif",
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/300170.cif",
    }
    assert result == expected


@pytest.mark.fast
def test_move_files(tmp_path: Path, cif_ensemble_test: CifEnsemble):
    file_paths = {
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/300171.cif",
        "tests/data/cif/ensemble_test/300170.cif",
    }
    dest_dir = tmp_path / "destination"
    initial_dir_path = "tests/data/cif/ensemble_test"
    initial_file_count = get_file_count(initial_dir_path)
    # Move files to the destination directory
    dest_dir_str = str(dest_dir)
    cif_ensemble_test.move_cif_files(file_paths, dest_dir_str)

    assert get_file_count(dest_dir_str) == initial_file_count - len(file_paths)
    cif_ensemble_test.move_cif_files(
        set(get_file_paths(dest_dir_str)), initial_dir_path
    )
    assert get_file_count(initial_dir_path) == initial_file_count


@pytest.mark.fast
def test_copy_files(tmp_path: Path, cif_ensemble_test: CifEnsemble):
    file_paths = {
        "tests/data/cif/ensemble_test/300169.cif",
        "tests/data/cif/ensemble_test/300171.cif",
        "tests/data/cif/ensemble_test/300170.cif",
    }
    dest_dir = tmp_path / "destination"
    dest_dir_str = str(dest_dir)
    # Move files to the destination directory
    cif_ensemble_test.copy_cif_files(file_paths, dest_dir_str)
    assert get_file_count(dest_dir_str) == len(file_paths)


"""
Test stats
"""


@pytest.mark.fast
def test_structure_stats(cif_ensemble_test):
    result = cif_ensemble_test.structure_stats
    expected = {"CeAl2Ga2": 3, "W": 3}
    assert result == expected


@pytest.mark.fast
def test_formula_stats(cif_ensemble_test):
    result = cif_ensemble_test.formula_stats
    expected = {"CeRu2Ge2": 1, "EuIr2Ge2": 1, "LaRu2Ge2": 1, "Mo": 3}
    assert result == expected


@pytest.mark.fast
def test_tag_stats(cif_ensemble_test):
    result = cif_ensemble_test.tag_stats
    expected = {"": 2, "hex": 1, "rt": 2, "rt_hex": 1}
    assert result == expected


@pytest.mark.fast
def test_space_group_number_stats(cif_ensemble_test):
    result = cif_ensemble_test.space_group_number_stats
    expected = {139: 3, 229: 3}
    assert result == expected


@pytest.mark.fast
def test_composition_type_stats(cif_ensemble_test):
    result = cif_ensemble_test.composition_type_stats
    expected = {1: 3, 3: 3}
    assert result == expected


@pytest.mark.fast
def test_space_group_name_stats(cif_ensemble_test):
    result = cif_ensemble_test.space_group_name_stats
    expected = {"I4/mmm": 3, "Im-3m": 3}
    assert result == expected


@pytest.mark.fast
def test_supercell_size_stats(cif_ensemble_test):
    result = cif_ensemble_test.supercell_size_stats
    expected = {54: 3, 360: 3}
    assert result == expected


@pytest.mark.fast
def test_min_distance_stats(cif_ensemble_test):
    result = cif_ensemble_test.min_distance_stats
    expected = {2.28: 1, 2.29: 1, 2.383: 1, 2.725: 2, 2.72: 1}
    assert result == expected


@pytest.mark.fast
def test_unique_elements_stats(cif_ensemble_test):
    result = cif_ensemble_test.unique_elements_stats
    expected = {
        "Ce": 1,
        "Eu": 1,
        "Ge": 3,
        "Ir": 1,
        "La": 1,
        "Mo": 3,
        "Ru": 2,
    }
    assert result == expected


@pytest.mark.fast
def test_unique_CN_values_by_min_dist_method_stat(cif_ensemble_test):
    result = cif_ensemble_test.unique_CN_values_by_min_dist_method_stat
    expected = {16: 3, 12: 3, 5: 2, 14: 3, 9: 1}
    assert result == expected


@pytest.mark.fast
def test_unique_CN_values_by_best_methods_stat(cif_ensemble_test):
    result = cif_ensemble_test.unique_CN_values_by_method_methods_stat
    expected = {16: 3, 10: 2, 12: 3, 14: 3, 9: 1}
    assert result == expected


"""
Test stat histograms
"""


@pytest.mark.slow
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
        "elements.png",
        "CN_by_min_dist_method.png",
        "CN_by_best_methods.png",
        "composition_type.png",
        "site_mixing_type.png",
    ]

    # Check that all expected files are created
    for file_name in expected_files:
        file_path = output_dir / file_name
        assert file_path.exists()
