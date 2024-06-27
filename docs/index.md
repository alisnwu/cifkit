# Getting Started

The purpose of this guide is to illustrate some of the main features that `cifkit` provides. It assumes a very basic knowledge of Python. The documentation is inspried by `scikit-learn.org`.

`cifkit` is an open source CIF library that supports supercell generation and visualization of files for high-throuhgput analysis. It also provides various tools for determining coordination numbers, plotting polyhedrons from each site based on the coordination numbers, bond fractions, move and copy .cif files based on a set of attributes, and determine atomic mixing information within 2-3 lines of code.

Some of the tools that built using `cifkit` are provided in 

### Projects based on `cifkit`

CIF Bond Analyzer (CBA) - extract and visualzie bnoding patterns - [DOI](https://doi.org/10.1016/j.jallcom.2023.173241) | [GitHub](https://github.com/bobleesj/cif-bond-analyzer)


## Insllation

```bash
pip install cifkit
```

## Start with CifEnsemble

```python
from cifkit import Cif, CifEnsemble
cif_enmsemble = CifEnsemble("tests/data/cif/ensemble_test")
cif_enmsemble = CifEnsemble("tests/data/cif/ensemble_test", add_nested_files=True)
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

### Filter files

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

### Move/copy



### Format


The following is an example with `Cif`

```python
from cifkit.models.cif import Cif

file_paths = folder.get_file_path_list("tests/data/cif/folder")

for file_path in file_paths:
    cif = Cif(file_path)
    print("Formula:", cif.formula)
    print("Unique element:", cif.unique_elements)
    print("Structure:", cif.structure)
    print("Site labels:", cif.site_labels)
    print("Space group:", cif.space_group_name)

    # Set the cut-off radius
    cut_off_radius = 4
    
    # Get all neartest neighbors from each site
    cif.compute_connections(cut_off_radius)
```

```python
filter_by_formulas
filter_by_structures
filter_by_space_group_names
filter_by_space_group_numbers
filter_by_site_mixing_types
filter_by_tags
filter_by_composition_types
filter_by_elements_containing
filter_by_elements_exact_matching


filter_by_CN_dist_method_containing
filter_by_CN_dist_method_exact_matching
filter_by_CN_best_methods_containing
filter_by_CN_best_methods_exact_matching
filter_by_min_distance
filter_by_supercell_count
```

## Generate stats
def move_cif_files(
    self, file_paths: set[str], to_directory_path: str
) -> None:
    """Move a set of CIF files to a destination directory."""
    move_files(to_directory_path, list(file_paths))

def copy_cif_files(
    self, file_paths: set[str], to_directory_path: str
) -> None:
    """Copy a set of CIF files to a destination directory."""
    copy_files(to_directory_path, list(file_paths))

def generate_stat_histograms(self, output_dir=None):
    plot_histograms(self, output_dir)
