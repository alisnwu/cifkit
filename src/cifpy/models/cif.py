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
from cifpy.preprocessors import environment
from cifpy.utils import prompt, folder


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

    def _generate_supercell(self):
        """Generate supercell information based on the unit cell data."""
        self.unitcell_points = get_supercell_points(self._block, 1)
        self.supercell_points = get_supercell_points(self._block, 3)
        self.unitcell_atom_count = get_cell_atom_count(self.unitcell_points)
        self.supercell_atom_count = get_cell_atom_count(self.supercell_points)

    def compute_connections(self, cutoff_radius=5.0, is_CN_used=False):
        """Compute nearest neighbor connections per site label."""
        self.connections = environment.get_site_connections(
            [self.site_labels, self.unitcell_lengths, self.unitcell_angles],
            self.unitcell_points,
            self.supercell_points,
            is_CN_used,
            cutoff_radius=cutoff_radius,
        )
        self._shortest_pair_distance = get_shortest_distance(self.connections)

    @property
    def shortest_pair_distance(self):
        """Property that checks if connections are computed and computes them if not."""
        if self.connections is None:
            self.compute_connections()  # Use default parameters or modify as needed
        return self._shortest_pair_distance

    def print_connected_points(self):
        prompt.log_conneted_points(self.connections)

    # prompt.log_conneted_points(cif.connections)


# TODO: Generate polyhedron .gif files
# TODO: Generate shortest atomic site information (CBA)
# TODO: Generate histograms
# TODO: Generate coordination numbers
