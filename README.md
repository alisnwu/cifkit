# cifkit

![Integration Tests](https://github.com/bobleesj/cifkit/actions/workflows/python-run-pytest.yml/badge.svg)
[![codecov](https://codecov.io/gh/bobleesj/cifkit/graph/badge.svg?token=AN2YAC337A)](https://codecov.io/gh/bobleesj/cifkit)
![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)
![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)
![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)
[![PyPi version](https://img.shields.io/pypi/v/cifkit.svg)](https://pypi.python.org/pypi/cifkit)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/bobleesj/cifkit/blob/main/LICENSE)

<!-- Open Codelab with a new tab -->
[![Open Google Codelab](https://img.shields.io/badge/Google%20Colab-Open-blue.svg)](https://colab.research.google.com/drive/1mZLFWyYblc2gxRqjP7CejZcUNGbQBzwo#scrollTo=DlB6ZTVaOMpq)


The documentation is available here: https://bobleesj.github.io/cifkit

![Logo light mode](assets/img/logo-black.png#gh-light-mode-only "cifkit logo light")
![Logo dark mode](assets/img/logo-color.png#gh-dark-mode-only "cifkit logo dark")

`cifkit` is designed to provide a set of well-organized and fully-tested utility
functions for handling large datasets, on the order of tens of thousands, of
`.cif` files.

> The current codebase and documentation are actively being improved as of July
> 8, 2024.

## Motivation

In high-throuhgput analysis using `.cif` files, the research project has identified the folowing needs:

- **Format files at once:** `.cif` files parsed from databases often contain
  ill-formatted files. We need a tool to standardize, preprocess, and filter out
  bad files. I also need to copy, move, and sort `.cif` files based on specific
  attributes.
- **Visualize coordination geometry:** We are interested in determining the
  coordination geometry and the best site in the supercell for analysis in a
  high-throughput manner. We need to identify the best site for each site label.
- **Visualize distribution of files:** We want to easily identify and categorize
  a distribution of underlying `.cif` files based on supercell size, tags,
  coordination numbers, elements, etc.

## Overview

Designed for individuals with minimal programming experience, `cifkit` provides
two primary objects: `Cif` and `CifEnsemble`.

### Cif

**`Cif`** is initialized with a `.cif` file path. It parses the .cif file,
preprocesses ill-formatted files, generates supercells, and computes nearest
neighbors. It also determines coordination numbers using four different methods
and generates polyhedrons for each site.

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

**`CifEnsemble`** is initialized with a folder path containing `.cif` files. It
identifies unique attributes, such as space groups and elements, across the
`.cif` files, moves and copies files based on these attributes. It generates
histograms for all attributes.

```python
from cifkit import CifEnsemble
from cifkit import Example

# Initialize
ensemble = CifEnsemble(Example.ErCoIn_folder_path)

# Get unique attributes
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

You may use example `.cif` files that can be easily imported, and you can visit
the documentation page [here](https://bobleesj.github.io/cifkit/).

## Installation

To install

```bash
pip install cifkit
```

You may need to download other dependencies:

```bash
pip install cifkit pyvista gemmi
```

`gemmi` is used for parsing `.cif` files. `pyvista` is used for plotting
polyhedrons.

## Visuals

### Polyhedron

You can visualize the polyhedron generated from each atomic site based on the
coordination number geoemtry. In our research, the goal is to map the structure
and coordination number with the physical property.

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

You can use `CifEnsemble` to visualize distributions of file counts based on
specific attributes, etc. Learn all features from the documentation provided
[here](https://bobleesj.github.io/cifkit/).

By formulas:

![Histogram](assets/img/histogram-formula.png)

By structures:

![Histogram](assets/img/histogram-structure.png)

## Project using cifkit

- CIF Bond Analyzer (CBA) - extract and visualize bonding patterns -
  [DOI](https://doi.org/10.1016/j.jallcom.2023.173241) |
  [GitHub](https://github.com/bobleesj/cif-bond-analyzer)
- CIF Cleaner - move, copy .cif files based on attributes -
  [GitHub](https://github.com/bobleesj/cif-cleaner)

## How to ask for help

`cifkit` is also designed for experimental materials scientists and chemists. If you
encounter any issues or have questions, please feel free to reach out or leave an issue. [![Star GitHub repository](https://img.shields.io/github/issues/bobleesj/cifkit.svg?style=social)](https://github.com/bobleesj/cifkit/stargazers)

## How to contribute


- [![Star GitHub repository](https://img.shields.io/github/stars/bobleesj/cifkit.svg?style=social)](https://github.com/bobleesj/cifkit/stargazers)
  the repository and recommend it to your colleagues who might find this
  repository helpful.
- [![Fork GitHub repository](https://img.shields.io/github/forks/bobleesj/cifkit?style=social)](https://github.com/bobleesj/cifkit/network/members)
  the repository and request a pull request for any changes.
- If you have any questions or have any suggestions, feel free to reach out to
  Sangjoon Bob Lee ([@bobleesj](https://github.com/bobleesj)) for any questions and feedback.

## Contributors

`cifkit` is made possible with contributions and support from the following
individuals:

- Anton Oliynyk: original ideation
- Alex Vtorov: polyhedron, testing
- Danila Shiryaev: testing, bug report
- Fabian Zills ([@PythonFZ](https://github.com/PythonFZ)): Tooling
  recommendations
- Emil Jaffal ([@EmilJaffal](https://github.com/EmilJaffal)): original testing,
  bug report
- Nikhil Kumar Barua: initial development
