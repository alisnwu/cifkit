from cifpy.utils import folder
from cifpy.utils.random import generate_random_numbers
from cifpy.figures.simple_histogram import generate_histogram


def test_generate_supercell_size_histogram():
    output_dir_path = "tests/data/cif/folder/plot"
    file_name = "supercell_histogram.png"
    output_file_path = folder.get_file_path(output_dir_path, file_name)
    supercell_settings = {
        "file_name": file_name,
        "title": "Histogram of supercell atom counts",
        "xlabel": "Number of atoms",
        "ylabel": "Frequency",
    }

    # Generate 100 random atom counts between 1000 to 3000
    atom_counts = generate_random_numbers(100, 1000, 3000, is_float=False)
    generate_histogram(atom_counts, output_dir_path, supercell_settings)

    assert folder.check_file_exists(output_file_path)
    assert folder.check_file_not_empty(output_file_path)


def test_generate_min_distance_histogram():
    output_dir_path = "tests/data/cif/folder/plot"
    file_name = "distance_histogram.png"
    output_file_path = folder.get_file_path(output_dir_path, file_name)
    distance_settings = {
        "file_name": file_name,
        "title": "Histogram of minimum bond distances",
        "xlabel": "Bond distance (Å)",
        "ylabel": "Frequency",
    }
    # Generate 100 random minimum distances between 2.0 Å and 4.0 Å
    min_dists = generate_random_numbers(100, 2.0, 4.0)
    generate_histogram(min_dists, output_dir_path, distance_settings)

    assert folder.check_file_exists(output_file_path)
    assert folder.check_file_not_empty(output_file_path)
