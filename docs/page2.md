
# Features

## `Cif`

- Get site pairs with atomic mixing information.
- Compute the coordination number using the d_min method.
- Identify homogeneous, heterogeneous, and all possible bond pairs.
- Parse tags from the third line, if provided.
- Compute the shortest distance.
- Preprocess symbolic labels with atomic mixing in CIF data.
- Remove author loop content.
- Generate a 2x2x2 supercell.
- Compute distances between element sites in CIF structures.
- Compute the coordination number.
- Extract unique tags, symmetry groups, symmetry names, supercell sizes, elements, structures, and formulas from CIF files.

## `CifEnsemble`

- Preprocess format and move files based on error.
- Copy files based on tags, symmetry group, symmetry name, supercell size, elements, structure, and formula.
- Move `.cif` files based on tags, symmetry group, symmetry name, supercell size, elements, structure distance, and coordination number.
- Generate histograms based on tags, symmetry group, symmetry name, supercell size, elements, structure, and formula.
- Get the minimum distance from each `.cif` file.
- Get all unique elements in all `.cif` files.


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
    cif_ensemble_test.unique_space_group_names
    # { "I4/mmm", "Im-3m"}
    
    cif_ensemble_test.unique_space_group_numbers
    # {139, 229}
    cif_ensemble_test.unique_tags
    # {"hex", "rt", "rt_hex", ""}

    assert cif_ensemble_test.minimum_distances