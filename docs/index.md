# Tutorials


## Cif

`Cif` is initialized with the .cif filepath. This object facilitates computing various distance metrics within crystal structures, generating supercells, and handling CIF data related to symmetry groups, elements, and chemical formulas.



The following is an example with `Cif`

```python
from cifpy.models.cif import Cif
from cifpy.utils import folder

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


## CifEnsemble

### Content

`CifEnsemble` offers features for preprocessing and querying CIF files, such as identifying unique bonding pairs and calculating coordination numbers. Additionally, CifPy supports operations like moving and copying files based on specific crystallographic tags and properties, and generating statistical histograms to visualize data distributions.


```python
cif_enmsemble = CifEnsemble("tests/data/cif/ensemble_test")

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
# [("tests/data/cif/ensemble_test/300169.cif", 2.29),
# ("tests/data/cif/ensemble_test/260171.cif", 2.72),
# ("tests/data/cif/ensemble_test/250697.cif", 2.725),
# ("tests/data/cif/ensemble_test/250709.cif", 2.725),
# ("tests/data/cif/ensemble_test/300171.cif", 2.383),
# ("tests/data/cif/ensemble_test/300170.cif", 2.28)]


cif_ensemble_test.supercell_atom_counts
# [("tests/data/cif/ensemble_test/300169.cif", 360),
# ("tests/data/cif/ensemble_test/260171.cif", 54),
# ("tests/data/cif/ensemble_test/250697.cif", 54),
# ("tests/data/cif/ensemble_test/250709.cif", 54),
# ("tests/data/cif/ensemble_test/300171.cif", 360),
# ("tests/data/cif/ensemble_test/300170.cif", 360)]

```

### Filter

```python
# Initialize
cif_enmsemble = CifEnsemble("tests/data/cif/ensemble_test")

# By formulas
cif_ensemble_test.filter_by_formulas(["LaRu2Ge2"]) 
cif_ensemble_test.filter_by_formulas(["LaRu2Ge2", "Mo"]) 

# By structures
cif_ensemble_test.filter_by_structures(["W"]) 
cif_ensemble_test.filter_by_structures("CeAl2Ga2") 

# By elements
cif_ensemble_test.filter_by_elements(["La"])
cif_ensemble_test.filter_by_elements(["Ge", "Ru"])

# By space group
cif_ensemble_test.filter_by_space_group_names("Im-3m")

# By space group numbers
cif_ensemble_test.filter_by_space_group_numbers([139])
```

### Move/copy


### Format


## Installation

```bash
pip install cifpy
pip install -e .
```

## Questions

Please feel free to ask any questions via bobleesj@gmail.com