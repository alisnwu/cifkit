# Getting started


## Statement of need

`cifkit` distinguishes itself from existing libraries creating and manipulating .cif files by offering higher-level
functions and variables that enable users to perform complex tasks efficiently
with a few lines of code. `cifkit` not only facilitates the visualization of
coordination geometry from each site but also extracts physics-based features
like volume and packing efficiency, crucial for structural analysis in ML tasks.
Additionally, it extracts atomic mixing information at the bond pair level—tasks
that would otherwise require extensive manual effort using GUI-based tools like
VESTA, Diamond, and CrystalMaker, due to the lack of readily available
higher-level functions.

Further enhancing its utility, cifkit excels in sorting, preprocessing, and
understanding the distribution of underlying CIF files. Common issues in CIF
files from databases, such as incorrect loop values and missing fractional
coordinates, are systematically addressed as cifkit standardizes and filters out
ill-formatted files. It also preprocesses atomic site labels, transforming
labels such as 'M1' to 'Fe1' in files with atomic mixing. Beyond error
correction, cifkit provides functionalities to copy, move, and sort files based
on attributes like coordination numbers, space groups, unit cells, and shortest
distances. It also excels in visualizing and cataloging CIF files, organizing
them based on supercell size, tags, coordination numbers, elements, and atomic
mixing, among other parameters.

## Overview

Designed for individuals with minimal programming experience, `cifkit` provides
two primary objects: `Cif` and `CifEnsemble`.

### Cif

**`Cif`** is initialized with a `.cif` file path. It parses the `.cif` file,
generates supercells, and computes nearest neighbors. It also determines
coordination numbers using four different methods and generates polyhedrons for
each site.

### CifEnsemble

**`CifEnsemble`** is initialized with a folder path containing `.cif` files. It
identifies unique attributes, such as space groups and elements, across the
`.cif` files, moves and copies files based on these attributes. It generates
histograms for all attributes.


## Research projects using `cifkit`

The below projects uses the `Cif` and `CifEnsemble` classes for research applications.

- CIF Bond Analyzer (CBA) - extract and visualize bonding patterns -
  [DOI](https://doi.org/10.1016/j.jallcom.2023.173241) |
  [GitHub](https://github.com/bobleesj/cif-bond-analyzer) | [Poster](https://bobleesj.github.io/files/presentation/2024-GRC-poster.pdf)
- Structure Analysis/Featurizer (SAF) - build geometric features for binary,
  ternary compounds -
  [GitHub](https://github.com/bobleesj/structure-analyzer-featurizer)
- CIF Cleaner - move, copy .cif files based on attributes
  [GitHub](https://github.com/bobleesj/cif-cleaner)

## How to ask for help

`cifkit` is also designed for experimental materials scientists and chemists.

- If you have any issues or questions, please feel free to reach out to Bob Lee [@bobleesj](https://github.com/bobleesj) or [leave an issue](https://github.com/bobleesj/cifkit/issues).

## How to contribute to `cifkit`

Here is how you can contribute to the `cifkit` project if you found it helpful:

- Star the repository on GitHub and recommend it to your colleagues who might
  find `cifkit` helpful as well.
  [![Star GitHub repository](https://img.shields.io/github/stars/bobleesj/cifkit.svg?style=social)](https://github.com/bobleesj/cifkit/stargazers)
- Create a new issue for any bugs or feature requests
  [here](https://github.com/bobleesj/cifkit/issues)
- Fork the repository and consider contributing changes via a pull request.
  [![Fork GitHub repository](https://img.shields.io/github/forks/bobleesj/cifkit?style=social)](https://github.com/bobleesj/cifkit/fork).
  Check out
  [CONTRIBUTING.md](https://github.com/bobleesj/cifkit/blob/main/CONTRIBUTING.md)
  for instructions.
- If you have any suggestions or need further clarification on how to use
  `cifkit`, please reach out to Bob Lee
  ([@bobleesj](https://github.com/bobleesj)).

## Contributors

`cifkit` has been greatly enhanced thanks to the contributions from a diverse
group of researchers:

- Anton Oliynyk: original ideation with `.cif` files
- Alex Vtorov: tool recommendation for polyhedron visualization
- Danila Shiryaev: testing as beta user
- Fabian Zills ([@PythonFZ](https://github.com/PythonFZ)): suggested tooling
  improvements
- Emil Jaffal ([@EmilJaffal](https://github.com/EmilJaffal)): initial testing
  and bug report
- Nikhil Kumar Barua: initial testing and bug report
- Nishant Yadav ([@sethisiddha1998](https://github.com/sethisiddha1998)):
  initial testing and bug report
- Siddha Sankalpa Sethi ([@runzsh](https://github.com/runzsh)): initial testing
  and bug report in initial testing and initial testing and bug report

We welcome all forms of contributions from the community. Your ideas and
improvements are valued and appreciated.

## Citation

Please consider citing `cifkit` if it has been useful for your research:

> Note: the `cifkit` manuscript is also under reviewed by the Journal of Open Source Software.

<a href="https://joss.theoj.org/papers/9016ae27b8c6fddffaae5aeb8be18d19"><img src="https://joss.theoj.org/papers/9016ae27b8c6fddffaae5aeb8be18d19/status.svg"></a>



## Other links

- [Developer guide](https://github.com/bobleesj/cifkit/blob/main/CONTRIBUTING.md)
- [MIT license](https://github.com/bobleesj/cifkit/blob/main/LICENSE)
