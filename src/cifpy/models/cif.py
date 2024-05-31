from cifpy.utils.cif_parser import (
    get_cif_block,
    get_loop_values,
    get_unitcell_lengths,
    get_unitcell_angles_rad,
    get_unique_site_labels,
    get_unique_elements_from_loop,
    get_unique_label_count,
    get_formula_structure_weight_s_group,
)

from cifpy.preprocessors.supercell import get_supercell_points
from cifpy.preprocessors.supercell_util import get_cell_atom_count
from cifpy.preprocessors import environment
from cifpy.utils import prompt, folder


class Cif:
    def __init__(self, file_path: str) -> None:
        """Initialize the Cif object with the file path."""
        self.file_path = file_path
        self.connections: dict = None  # Initialize nearest neighbor as None
        self._load_data()

    def _load_data(self):
        """Load data from the .cif file and process it."""
        self._block = get_cif_block(self.file_path)
        self._parse_cif_data()
        self._generate_supercell()

    def _parse_cif_data(self):
        """Parse the main CIF data from the block."""
        self._loop_values = get_loop_values(self._block)
        self.unitcell_lengths = get_unitcell_lengths(self._block)
        self.unitcell_angles = get_unitcell_angles_rad(self._block)
        self.site_labels = get_unique_site_labels(self._loop_values)
        self.unique_elements = get_unique_elements_from_loop(self._loop_values)
        (
            self.formula,
            self.structure,
            self.weight,
            self.space_group_number,
            self.space_group_name,
        ) = get_formula_structure_weight_s_group(self._block)

    def _generate_supercell(self):
        """Generate supercell information based on the unit cell data."""
        self.unitcell_points = get_supercell_points(self._block, 1)
        self.supercell_points = get_supercell_points(self._block, 3)
        self.unitcell_atom_count = get_cell_atom_count(self.unitcell_points)
        self.supercell_atom_count = get_cell_atom_count(self.supercell_points)


#     def compute_connections(self, cutoff_radius=5.0):
#         """
#         Compute nearest neighbor connections per site label. It is not called
#         during initialization due to extensive computation.
#         """
#         if not self.connections:
#             self.connections = environment.get_site_connections(
#                 self.site_labels,
#                 self.unitcell_points,
#                 self.supercell_points,
#                 self.unitcell_lengths,
#                 self.unitcell_angles,
#                 False,
#                 cutoff_radius=cutoff_radius,
#             )


# # TODO - Store the shortest distance per pair, Store the shortest distances per pair

# Usage example

file_paths = folder.get_file_path_list("tests/data/cif/folder")
for file_path in file_paths:
    cif = Cif(file_path)
    print(cif.file_path)
    print(cif.unique_elements)
    print(cif.formula)
    print(cif.unique_elements)
    print(cif.structure)
    print(cif.site_labels)
    print(cif.unitcell_atom_count)
    print(cif.supercell_atom_count)
    print(cif.space_group_name)
    print(cif.space_group_number)
    # cif.compute_connections()  # Computes and stores the connections
    # print(cif.connections)
    print()
