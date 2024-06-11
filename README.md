# CifPy

CifPy is a Python toolkit for high-throughput analysis of .cif files

## Tasks

- CifEnsmeble: format and preprocess all .cif files
- CifEnsemble: check and move ill-formatted files.
- CifEnsemble: generate histograms on cif attributes
- Test: include coverage percent
- Test: include supported Python versions
- Test: include requirements.txt
- Test: include GitHub integration test
- GitHub: include contribution
- GitHub: include GitHub pull request/issue template
- Doc: write features/tutorials
- Doc: host the documentation

## Motivation

- I build high-throughput analysis tools using `.cif` files for research. The tools analyze bonding distances, site analysis, and coordination numbers.
- Each tool requires preprocesing, formatting, copying, moving, and sorting .cif files.
- To streamline the above tasks, I developed `CifPy` that can be easily imported for the above tasks.

## Overview

CifPy provides two simple objects `Cif` and `CifEnsemble`.

`Cif` is initialized with the `.cif` filepath. This object facilitates computing various distance metrics within crystal structures, generating supercells, and handling CIF data related to symmetry groups, elements, and chemical formulas.

`CifEnsemble` offers features for preprocessing and querying `.cif` files, such as identifying unique bonding pairs and calculating coordination numbers. Additionally, CifPy supports operations like moving and copying files based on specific crystallographic tags and properties, and generating statistical histograms to visualize data distributions.

## Documentation

Please see the tutorial provided here (TBA).

## Installation

To run locally:

```bash
pip install -e .
```
