from cifpy.utils.random import generate_random_numbers

from cifpy.figures.simple_histogram import generate_histogram


def test_generate_supercell_size_histogram():
    dir_path = "tests/data/cif/folder"
    supercell_settings = {
        "file_name": "supercell_histogram.png",
        "title": "Histogram of supercell atom counts",
        "xlabel": "Number of atoms",
        "ylabel": "Frequency",
    }

    supercell_atom_counts = generate_random_numbers(
        100, 1000, 3000, is_float=False
    )
    generate_histogram(
        supercell_atom_counts, dir_path, supercell_settings
    )


def test_generate_min_distance_histogram():
    dir_path = "tests/data/cif/folder"
    distance_settings = {
        "file_name": "distance_histogram.png",
        "title": "Histogram of minimum bond distances",
        "xlabel": "Bond distance (Å)",
        "ylabel": "Frequency",
    }
    # Generate 100 random minimum distances between 2.0 Å and 4.0 Å
    min_dists = generate_random_numbers(100, 2.0, 4.0)
    generate_histogram(min_dists, dir_path, distance_settings)
