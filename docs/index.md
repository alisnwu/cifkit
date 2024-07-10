# Getting started

The purpose of this guide is to illustrate some of the main features that
`cifkit` provides. It assumes a very basic knowledge of Python.

`cifkit` is an open source CIF library that supports supercell generation and
provide tools for high-throuhgput analysis. It also provides various tools for
determining coordination numbers, plotting polyhedrons from each site based on
the coordination numbers, bond fractions, move and copy `.cif` files based on a
set of attributes, and determine atomic mixing information in 2-3 lines of code.

## Installation

Install `cifkit` via:

```bash
pip install cifkit
```

You may need to download other dependencies:

```bash
pip install cifkit pyvista gemmi
```

`gemmi` is used for parsing `.cif` files. `pyvista` is used for plotting
polyhedrons.

## Start with CifEnsemble

`cifkit` offers a class called `CifEnsemble` which handles many `.cif` files in
a high-throuhgput way. You can initialize the object using the folder path
containing `.cif` files shown below.

```python
from cifkit import CifEnsemble

# Initialize
ensemble = CifEnsemble("tests/data/cif/ensemble_test")

# Initialize including nested files
ensemble = CifEnsemble("tests/data/cif/ensemble_test", add_nested_files=True)

# Folder path
ensemble.cif_folder_path
# "tests/data/cif/ensemble_test"

```

If you do not have `.cif` files for testing, `cifkit` also provides a set of
`.cif` files accessible.

```python
from cifkit import CifEnsemble, Example
from cifkit import Example

# Initalize with the file path
ensemble = CifEnsemble(Example.ErCoIn_big_folder_path)
```

### Get unique attributes

Use the `ensemble` object to get unique attributes such as elements, formulas,
etc.

```python
# Unique formulas
ensemble.unique_formulas
# {"EuIr2Ge2", "CeRu2Ge2", "LaRu2Ge2", "Mo"}

# Unique structures
ensemble.unique_structures
# {"CeAl2Ga2", "W"}

# Unique elements
ensemble.unique_elements
# {"La", "Ru", "Ge", "Ir", "Eu", "Ce", "Mo"}

# Unique space group names
ensemble.unique_space_group_names
# {"I4/mmm", "Im-3m"}

# Unique space group numbers
ensemble.unique_space_group_numbers
# {139, 229}

# Unique tags
ensemble.unique_tags
# {"hex", "rt", "rt_hex", ""}
```

### Get distances and supercell size per file

The following computes the size of each supercell and the minimum distance per
file.

```python
# Get min distance per file
ensemble.minimum_distances
# [("tests/data/cif/ensemble_test/250709.cif", 2.725),
# ("tests/data/cif/ensemble_test/300171.cif", 2.383),
# ("tests/data/cif/ensemble_test/300170.cif", 2.28)]

# Get supercell size per file
ensemble_test.supercell_atom_counts
# [("tests/data/cif/ensemble_test/250709.cif", 54),
# ("tests/data/cif/ensemble_test/300171.cif", 360),
# ("tests/data/cif/ensemble_test/300170.cif", 360)]
```

### Filter files by attributes

The following returns a set of file paths to each `.cif` file.

```python
# By formulas
ensemble_test.filter_by_formulas(["LaRu2Ge2"])
ensemble_test.filter_by_formulas(["LaRu2Ge2", "Mo"])

# By structures
ensemble_test.filter_by_structures(["W"])
ensemble_test.filter_by_structures("CeAl2Ga2")

# By space group
ensemble_test.filter_by_space_group_names("Im-3m")

# By space group numbers
ensemble_test.filter_by_space_group_numbers([139])
```

### Move and copy files

Now you have a set of file paths with example below, you can copy and move files
to a specific directroy. For high-throuhgout analysis, you might be interested
in separating files based on tags, elements, coordination numbers, etc.

```python
file_paths = {
    "tests/data/cif/ensemble_test/300169.cif",
    "tests/data/cif/ensemble_test/300171.cif",
    "tests/data/cif/ensemble_test/300170.cif",
}

# To move files
ensemble.move_cif_files(file_paths, dest_dir_path)

# To copy files
ensemble.copy_cif_files(file_paths, dest_dir_path)
```

## Are you ready?

Now, if you are interested in working with individual `.cif` files and learn
more about all features in `cifkit`, let's visit the `Example notebooks` section
[here](https://bobleesj.github.io/cifkit/notebooks/00_Intro/)!

## Research projects using `cifkit`

- CIF Bond Analyzer (CBA) - extract and visualize bonding patterns -
  [DOI](https://doi.org/10.1016/j.jallcom.2023.173241) |
  [GitHub](https://github.com/bobleesj/cif-bond-analyzer)
- CIF Cleaner - move, copy .cif files based on attributes -
  [GitHub](https://github.com/bobleesj/cif-cleaner)
- Structure Analysis/Featurizer (SAF) - build geometric features for binary,
  ternary compounds -
  [GitHub](https://github.com/bobleesj/structure-analyzer-featurizer)
