# cifkit: Python toolkit for high-throughput analysis of CIF files

cifkit is designed for the high-throughput analysis of Crystallographic Information File (.cif) formats. In just 2-4 lines of code,

- preprocess .cif files for high-throuhgput processing
- move, copy, filter files based on a comprehensive set of attributes such as coordination number, elements, tags
- determine nearest neighbor and coordination environments at each site
- facilitate the plotting of polyhedrons and 

## Overview

cifkit provides two primary objects: `Cif` and `CifEnsemble`.

- **`Cif`**: Initializes with a `.cif` file path. It parses the .cif file, preprocesses ill-formatted files, generates supercells, and computes nearest neighbors. It also determines coordination numbers using four different methods and generates polyhedrons for each site.

- **`CifEnsemble`**: Initializes with a folder path containing `.cif` files. It identifies unique attributes, such as space groups and elements, across the .cif files, moves and copies files based on these attributes. It generates histograms for all attribute.

## Motivation

- High throughput analysis tools using `.cif` files for research. The tools analyze bonding distances, site analysis, and coordination numbers.
- Each tool requires preprocesing, formatting, copying, moving, and sorting .cif files.
- To streamline the above tasks, I developed `CifPy` that can be easily imported for the above tasks.


## Documentation

Please see the tutorial provided here (TBA).

## Installation

To run locally:

```bash
pip install -e .
```

## Developer

Sangjoon Bob Lee (@bobleesj)

### MkDocs

```bash
pip install mkdocstrings
pip install mkdocstrings-python
pip install mkdocs         
pip install mkdocs-material
pip install mkdocs-jupyter
mkdocs serve
```ls