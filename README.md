# cifkit

![Logo light mode](assets/img/logo-black.png#gh-light-mode-only "cifkit logo light")
![Logo dark mode](assets/img/logo-color.png#gh-dark-mode-only "cifkit logo dark")


`cifkit` is designed to provide a set of well-organized and fully-tested utility functions for handling a large set on the order of ten of thousands of `.cif` files.

> The current codebase and documentation are actively improved. July 3, 2024

## Motivation

Since Summer 2023, I have been building interactive tools that analyze `.cif` files. I have noticed the following needs:

- **Format files at once:** `.cif` files parsed from databases often have ill-formatted files. We need a tool to standardize, preprocess, and filter bad files. I also need to copy, move, and sort `.cif` files based on specific attributes.
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


## Project using cifkit

- CIF Bond Analyzer (CBA) - extract and visualize bonding patterns - [DOI](https://doi.org/10.1016/j.jallcom.2023.173241) | [GitHub](https://github.com/bobleesj/cif-bond-analyzer)


## How to Ask for Help or Contribute

`Cifkit` is also designed for experimental materials scientists and chemists. If you encounter any issues or have questions, please feel free to reach out via the email listed on my GitHub profile. My goal is to ensure `cifkit` is accessible and easy to use for everyone.

## Asking for Support

This is my first open-source project. If `cifkit` has been useful in your research, you could help me by taking 2-3 seconds to "star" this repository.

## Visuals

### Polyhedron

You can visualize the polyhedron generated from each atomic site based on the coordination number geoemtry. In our research, the goal is to map the structure and coordination number with the physical property.

```python
from cifkit import Cif

# Example usage
cif = Cif("your_cif_file_path")
site_labels = cif.site_labels

# Loop through each site
for label in site_labels:
    # Dipslay each polyhedron, a file saved for each
    cif.plot_polyhedron(label, is_displayed=True)
```

![Polyhedron generation](assets/img/ErCoIn_polyhedron.png)

### Histograms

You can use `CifEnsemble` to visualize distributions of file counts based on specific attributes, etc. Learn all features from the documentation provided [here](https://bobleesj.github.io/cifkit/).

By formulas:

![Histogram](assets/img/histogram-formula.png)

By structures:

![Histogram](assets/img/histogram-structure.png)
