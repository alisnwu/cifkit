# cifkit

![Logo light mode](assets/img/logo-black.png#gh-light-mode-only "cifkit logo light")
![Logo dark mode](assets/img/logo-color.png#gh-dark-mode-only "cifkit logo dark")


`cifkit` is designed to provide a set of well-organized and fully-tested utility functions for handling a large set on the order of ten of thousands of `.cif` files.

> The current codebase and documentation are actively improved.

## Motivation

I have been building interactive tools that analyze `.cif` files. I have noticed the following needs:

- **Format files at once:** In my research, I noticed that `.cif` files parsed from databases often have ill-formatted files. We need a tool to standardize, preprocess, and filter bad files. I also need to copy, move, and sort `.cif` files based on specific attributes.
- **Visualize coordination geometry:** We are interested in determining the coordination geometry and the best site in the supercell for analysis in a high-throughput manner. We need to identify the best site for each site label.
- **Visualize distribution of files:** We want to easily identify and categorize a distribution of underlying `.cif` files based on supercell size, tags, coordination numbers, elements, etc.

## Overview

Designed for people with minimal programming experience, cifkit provides two primary objects: `Cif` and `CifEnsemble`.

### Cif

**`Cif`** is Initialized with a `.cif` file path. It parses the .cif file, preprocesses ill-formatted files, generates supercells, and computes nearest neighbors. It also determines coordination numbers using four different methods and generates polyhedrons for each site.

```python
from cifkit import Cif
from cifkit import Example

# Initalize with the example file provided
cif = Cif(Example.Er10Co9In20_file_path)

# Print attributes
print("File name:", cif.file_name)
print("Formula:", cif.formula)
print("Unique element:", cif.unique_elements)
```

### CifEnsemble

**`CifEnsemble`** is initialized with a folder path containing `.cif` files. It identifies unique attributes, such as space groups and elements, across the `.cif` files, moves and copies files based on these attributes. It generates histograms for all attributes.


 ```python
from cifkit import CifEnsemble
from cifkit import Example

# Initialize
ensemble = CifEnsemble("tests/data/cif/ensemble_test")
ensemble.unique_formulas
ensemble.unique_structures
ensemble.unique_elements
ensemble.unique_space_group_names
ensemble.unique_space_group_numbers
ensemble.unique_tags
ensemble.minimum_distances
ensemble_test.supercell_atom_counts
```

## Tutorial and documentation

I provide example `.cif` files that can be easily imported, and you can visit the documentation page [here](https://bobleesj.github.io/cifkit/)!

## Installation

To install

```
pip install cifkit
```

You may need to download other dependencies:

```
pip install cifkit pyvista gemmi
```

`gemmi` is used for parsing `.cif` files. `pyvista` is used for plotting polyhedrons.


## Developer

Sangjoon Bob Lee ([@bobleesj](https://github.com/bobleesj))

## Project using cifkit

- CIF Bond Analyzer (CBA) - extract and visualize bonding patterns - [DOI](https://doi.org/10.1016/j.jallcom.2023.173241) | [GitHub](https://github.com/bobleesj/cif-bond-analyzer)


## Images

![Polyhedron generation](assets/img/ErCoIn_polyhedron.png)
