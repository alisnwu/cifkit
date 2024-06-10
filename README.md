# CifPy

CifPy provides two simple objects `Cif` and `CifEnsemble`.

`Cif` is initialized with the `.cif` filepath. This object facilitates computing various distance metrics within crystal structures, generating supercells, and handling CIF data related to symmetry groups, elements, and chemical formulas.

`CifEnsemble` offers features for preprocessing and querying `.cif` files, such as identifying unique bonding pairs and calculating coordination numbers. Additionally, CifPy supports operations like moving and copying files based on specific crystallographic tags and properties, and generating statistical histograms to visualize data distributions.

## Tutorials

## Example

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

## Development

To run locally:

```bash
pip install -e .
```
