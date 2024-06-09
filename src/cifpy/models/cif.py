from cifpy.utils.cif_parser import (
    get_cif_block,
    get_loop_values,
    get_unitcell_lengths,
    get_unitcell_angles_rad,
    get_unique_site_labels,
    get_unique_elements_from_loop,
    get_formula_structure_weight_s_group,
    get_tag_from_third_line,
)

from cifpy.coordination.distance import get_shortest_distance
from cifpy.preprocessors.supercell import get_supercell_points
from cifpy.preprocessors.supercell_util import get_cell_atom_count
from cifpy.preprocessors.environment import (
    get_site_connections,
    filter_connections_with_cn,
)
from cifpy.utils import prompt, folder
from cifpy.utils.bond_pair import (
    get_heterogenous_element_pairs,
    get_homogenous_element_pairs,
)


class Cif:
    def __init__(self, file_path: str) -> None:
        """Initialize the Cif object with the file path."""
        self.file_path = file_path
        self.connections = None  # Private attribute to store connections
        self._shortest_pair_distance = None
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
        self.tag = get_tag_from_third_line(self.file_path)
        self.heterogeneous_bond_pairs = get_heterogenous_element_pairs(
            self.formula
        )
        self.homogenous_bond_pairs = get_homogenous_element_pairs(self.formula)
        self.all_bond_pairs = (self.heterogeneous_bond_pairs).union(
            self.homogenous_bond_pairs
        )

    def _generate_supercell(self):
        """Generate supercell information based on the unit cell data."""
        self.unitcell_points = get_supercell_points(self._block, 1)
        self.supercell_points = get_supercell_points(self._block, 3)
        self.unitcell_atom_count = get_cell_atom_count(self.unitcell_points)
        self.supercell_atom_count = get_cell_atom_count(self.supercell_points)

    def compute_connections(self, cutoff_radius=10.0):
        """Compute nearest neighbor connections per site label."""
        self.connections = get_site_connections(
            [
                self.site_labels,
                self.unitcell_lengths,
                self.unitcell_angles,
            ],
            self.unitcell_points,
            self.supercell_points,
            cutoff_radius=cutoff_radius,
        )
        self._shortest_pair_distance = get_shortest_distance(self.connections)
        self._connections_CN = filter_connections_with_cn(self.connections)

    @property
    def shortest_pair_distance(self):
        """Property that checks if connections are computed and computes them if not."""
        if self.connections is None:
            self.compute_connections()  # Use default parameters or modify as needed
        return self._shortest_pair_distance

    @property
    def connections_CN(self):
        """Property that checks if connections are computed and computes them if not."""
        if self.connections is None:
            self.compute_connections()  # Use default parameters or modify as needed
        return self._shortest_pair_distance

    def print_connected_points(self):
        prompt.log_conneted_points(self.connections)
