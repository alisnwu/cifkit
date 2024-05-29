from cifpy.utils.cif_parser import (
    get_cif_block,
    get_loop_values,
    get_unitcell_lengths,
    get_unitcell_angles_rad,
    get_unique_site_labels,
    get_unique_elements,
    get_unique_label_count,
)

from cifpy.preprocessors.supercell import get_supercell_points
from cifpy.preprocessors.supercell_util import get_cell_atom_count
from cifpy.preprocessors import environment
from cifpy.utils import prompt, folder


class Cif:
    def __init__(self, file_path: str) -> None:
        """
        Initialize an object containing parsed .cif file information.
        """
        self.file_path = file_path
        self._block = get_cif_block(self.file_path)
        self._loop_values = get_loop_values(self._block)

        # Parse .cif file
        self.unitcell_lengths = get_unitcell_lengths(self._block)
        self.unitcell_angles = get_unitcell_angles_rad(self._block)
        self.site_labels = get_unique_site_labels(self._loop_values)
        self.unique_elements = get_unique_elements(self._loop_values)
        self.unique_label_count = get_unique_label_count(self._loop_values)

        # Generate supercell
        self.unitcell_points = get_supercell_points(self._block, 1)
        self.supercell_points = get_supercell_points(self._block, 3)
        self.unitcell_atom_count = get_cell_atom_count(self.unitcell_points)
        self.supercell_atom_count = get_cell_atom_count(self.supercell_points)

        # Connections are not computed during initialization
        self.connections = None

    def compute_connections(self, cutoff_radius=5.0):
        """
        Compute nearest neighbor connections per site label. It is not called
        during initialization due to extensive computation.
        """
        if not self.connections:
            self.connections = environment.get_all_labels_connections(
                self.site_labels,
                self.unitcell_points,
                self.supercell_points,
                self.unitcell_lengths,
                self.unitcell_angles,
                False,
                cutoff_radius=cutoff_radius,
            )

# Usage example
file_paths = folder.get_file_path_list("tests/data/cif/large")
for file_path in file_paths:
    cif = Cif(file_path)
    print(cif.file_path)
    print(cif.unique_elements)
    print(cif.site_labels)
    print(cif.unitcell_atom_count)
    print(cif.supercell_atom_count)
    cif.compute_connections()  # Computes and stores the connections
    print(cif.connections)
    
