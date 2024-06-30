from cifkit import Cif, CifEnsemble
from cifkit.utils import folder

# Example usage

cif_ensemble = CifEnsemble("tests/data/cif/no_radius_data")

for cif in cif_ensemble.cifs:
    site_labels = cif.site_labels

    print("Processing", cif.formula, cif.file_name)
    print("size", cif.supercell_atom_count)
    for label in site_labels:
        cif.plot_polyhedron(label)


# cif_ensemble.generate_stat_histograms(display=True)
