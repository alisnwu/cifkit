from cifkit import Cif, CifEnsemble
from cifkit.utils import folder

# Example usage

cif_ensemble = CifEnsemble("tests/data/cif/polyhedron_error")

for cif in cif_ensemble.cifs:
    site_labels = cif.site_labels
    print("Procesing", cif.formula, cif.file_name)
    for label in site_labels:
        cif.plot_polyhedron(label)
