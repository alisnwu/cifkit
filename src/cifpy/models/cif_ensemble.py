from cifpy.models.cif import Cif

# Compute all supercell size distribution
# Compute all unitcell size distribution
# Compute all minimum distance distribution
# Compute all minimum distances per pair
# Compute the most coordination number for each site


class CifEnsemble:
    def __init__(self):
        self.cif_files = []

    def add_cif(self, cif):
        self.cif_files.append(cif)

    def compute_unitcell_size_distribution(self):
        # Compute all supercell size distribution
        pass

    def compute_supercell_size_distribution(self):
        # Compute all supercell size distribution
        pass

    def compute_element_statistics(self):
        pass


# Usage
ensemble = CifEnsemble()
ensemble.add_cif(Cif("file1.cif"))
ensemble.add_cif(Cif("file2.cif"))
stats = ensemble.compute_statistical_metrics()
predictions = ensemble.ensemble_predictions()
