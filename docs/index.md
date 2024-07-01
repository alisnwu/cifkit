# Getting Started

The purpose of this guide is to illustrate some of the main features that `cifkit` provides. It assumes a very basic knowledge of Python.

`cifkit` is an open source CIF library that supports supercell generation and provide tools for high-throuhgput analysis. It also provides various tools for determining coordination numbers, plotting polyhedrons from each site based on the coordination numbers, bond fractions, move and copy `.cif` files based on a set of attributes, and determine atomic mixing information in 2-3 lines of code.

## Installation

```bash
pip install cifkit
```

## Start with CifEnsemble

```python
from cifkit import CifEnsemble
ensemble = CifEnsemble("tests/data/cif/ensemble_test")
ensemble = CifEnsemble("tests/data/cif/ensemble_test", add_nested_files=True)
```

### Get unique attributes

```
cif_ensemble.cif_folder_path
# "tests/data/cif/ensemble_test"

cif_ensemble.unique_formulas
# {"EuIr2Ge2", "CeRu2Ge2", "LaRu2Ge2", "Mo"}

cif_ensemble.unique_structures
# {"CeAl2Ga2", "W"}

cif_ensemble.unique_elements
# {"La", "Ru", "Ge", "Ir", "Eu", "Ce", "Mo"}

cif_ensemble.unique_space_group_names
# { "I4/mmm", "Im-3m"}

cif_ensemble.unique_space_group_numbers
# {139, 229}

cif_ensemble.unique_tags
# {"hex", "rt", "rt_hex", ""}

cif_ensemble.minimum_distances
# [("tests/data/cif/ensemble_test/250709.cif", 2.725),
# ("tests/data/cif/ensemble_test/300171.cif", 2.383),
# ("tests/data/cif/ensemble_test/300170.cif", 2.28)]

cif_ensemble_test.supercell_atom_counts
# [("tests/data/cif/ensemble_test/250709.cif", 54),
# ("tests/data/cif/ensemble_test/300171.cif", 360),
# ("tests/data/cif/ensemble_test/300170.cif", 360)]
```

### Filter files by attributes

```python
# By formulas
cif_ensemble_test.filter_by_formulas(["LaRu2Ge2"]) 
cif_ensemble_test.filter_by_formulas(["LaRu2Ge2", "Mo"]) 

# By structures
cif_ensemble_test.filter_by_structures(["W"]) 
cif_ensemble_test.filter_by_structures("CeAl2Ga2") 

# By space group
cif_ensemble_test.filter_by_space_group_names("Im-3m")

# By space group numbers
cif_ensemble_test.filter_by_space_group_numbers([139])
```

## Features

### `Cif`

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

### `CifEnsemble`

- Preprocess format and move files based on errors.
- Copy files based on tags, symmetry group, symmetry name, supercell size, elements, structure, and formula.
- Move `.cif` files based on tags, symmetry group, symmetry name, supercell size, elements, structure distance, and coordination number.
- Generate histograms based on tags, symmetry group, symmetry name, supercell size, elements, structure, and formula.
- Get the minimum distance from each `.cif` file.
- Get all unique elements in all `.cif` files.

### Projects based on `cifkit`

- CIF Bond Analyzer (CBA) - extract and visualzie bnoding patterns - [DOI](https://doi.org/10.1016/j.jallcom.2023.173241) | [GitHub](https://github.com/bobleesj/cif-bond-analyzer)

