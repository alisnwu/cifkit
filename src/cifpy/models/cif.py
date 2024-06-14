"""
Import statements placed bottom to avoid cluttering.
"""

# Polyhedron
from cifpy.figures import polyhedron


# Parser .cif file
from cifpy.utils.cif_parser import (
    get_cif_block,
    get_loop_values,
    get_unitcell_lengths,
    get_unitcell_angles_rad,
    get_unique_site_labels,
    get_unique_elements_from_loop,
    get_formula_structure_weight_s_group,
    get_tag_from_third_line,
    parse_atom_site_occupancy_info,
    check_unique_atom_site_labels,
)

# Edit .cif file
from cifpy.preprocessors.format import preprocess_label_element_loop_values
from cifpy.utils.cif_editor import remove_author_loop

# Supercell generation
from cifpy.preprocessors.supercell import get_supercell_points
from cifpy.preprocessors.supercell_util import get_cell_atom_count
from cifpy.preprocessors.environment import (
    get_site_connections,
    get_CN_connections_by_min_dist_method,
)


# Radius
from cifpy.data.radius_handler import (
    get_is_radius_data_available,
    get_radius_values_per_element,
    compute_radius_sum,
)

# Coordination number
from cifpy.preprocessors.environment_util import flat_site_connections
from cifpy.coordination.composition import (
    get_bond_counts,
    get_bond_fractions,
    get_CN_values,
    get_avg_CN,
    get_unique_CN_values,
)
from cifpy.coordination.method import compute_CN_max_gap_per_site
from cifpy.coordination.filter import (
    find_best_polyhedron,
    get_CN_connections_by_best_method,
)

# Bond pair
from cifpy.coordination.bond_distance import (
    get_shortest_distance_per_bond_pair,
)

# Site info
from cifpy.coordination.site_distance import (
    get_shortest_distance,
    get_shortest_distance_per_site,
)
from cifpy.coordination.geometry import get_polyhedron_coordinates_labels

from cifpy.utils import prompt
from cifpy.utils.bond_pair import (
    get_heterogenous_element_pairs,
    get_homogenous_element_pairs,
    get_all_bond_pairs,
)

from cifpy.occupacny.mixing import get_site_mixing_type


class Cif:
    def __init__(self, file_path: str) -> None:
        """Initialize the Cif object with the file path."""
        self.file_path = file_path
        self.connections = None  # Private attribute to store connections
        self._shortest_pair_distance = None
        self._preprocess()
        self._load_data()

    def _preprocess(self):
        """Preprocess each .cif file and check any error."""
        check_unique_atom_site_labels(self.file_path)
        remove_author_loop(self.file_path)
        preprocess_label_element_loop_values(self.file_path)

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
        self.composition_type = len(self.unique_elements)
        self.tag = get_tag_from_third_line(self.file_path)
        self.atom_site_info = parse_atom_site_occupancy_info(self.file_path)
        self.heterogeneous_bond_pairs = get_heterogenous_element_pairs(
            self.formula
        )
        self.homogenous_bond_pairs = get_homogenous_element_pairs(self.formula)
        self.all_bond_pairs = get_all_bond_pairs(self.formula)
        self.site_mixing_type = get_site_mixing_type(self._loop_values)
        self.is_radius_data_available = get_is_radius_data_available(
            self.unique_elements
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

        # Get flattened connections
        self._connections_flattened = flat_site_connections(self.connections)

        # Get shortest distance, per bond pair, per site
        self._shortest_pair_distance = get_shortest_distance(self.connections)
        self._shortest_distance_per_bond_pair = (
            get_shortest_distance_per_bond_pair(self.connections_flattened)
        )
        self._shortest_distance_per_site = get_shortest_distance_per_site(
            self.connections
        )

        self._radius_values_per_element = get_radius_values_per_element(
            self.unique_elements, self.shortest_dist_per_bond_pair
        )
        self._radius_sum_per_bond = compute_radius_sum(self.radius_values)

        # Get coordination numbers using the min dist method
        self._CN_connections_by_min_dist_method = (
            get_CN_connections_by_min_dist_method(self.connections)
        )
        # Get max gaps per label
        self._CN_max_gap_per_site = compute_CN_max_gap_per_site(
            self._radius_sum_per_bond, self.connections, self.site_mixing_type
        )

        # Determine the best polyhedron
        self._best_CN_polyhedrons = find_best_polyhedron(
            self._CN_max_gap_per_site, self.connections
        )

        # Determine the best CN connections
        self._CN_connections_by_best_method = (
            get_CN_connections_by_best_method(
                self._best_CN_polyhedrons, self.connections
            )
        )

    def get_polyhedron_labels_from_site(
        self, label: str
    ) -> tuple[list[list[float]], list[str]]:
        if self.compute_connections is None:
            self.compute_connections()
        return get_polyhedron_coordinates_labels(
            self.CN_connections_by_min_dist_method, label
        )

    # Connections
    def get_connections_bond_counts(self, connections):
        if self.connections is None:
            self.compute_connections()
        return get_bond_counts(self.formula, connections)

    def get_connections_bond_fractions(self, connections):
        if self.connections is None:
            self.compute_connections()
        bond_counts = get_bond_counts(self.formula, connections)
        return get_bond_fractions(bond_counts)

    def get_connections_coordination_numbers(self, connections):
        if self.connections is None:
            self.compute_connections()
        return get_CN_values(connections)

    def get_connections_average_coordination_number(self, connections):
        if self.connections is None:
            self.compute_connections()
        return get_avg_CN(connections)

    def get_connections_unique_coordination_numbers(self, connections):
        if self.connections is None:
            self.compute_connections()
        return get_unique_CN_values(connections)

    def plot_polyhedron(self, site_label, output_dir=None):
        if self.connections is None:
            self.compute_connections()
        coords, labels = get_polyhedron_coordinates_labels(
            self.CN_connections_by_min_dist_method, site_label
        )
        polyhedron.plot(coords, labels, self.file_path, output_dir)

    @property
    def shortest_pair_distance(self):
        """Property that checks if connections are computed and computes."""
        if self.connections is None:
            self.compute_connections()
        return self._shortest_pair_distance

    @property
    def shortest_dist_per_bond_pair(self):
        if self.connections is None:
            self.compute_connections()
        return self._shortest_distance_per_bond_pair

    @property
    def shortest_distance_per_site(self):
        if self.connections is None:
            self.compute_connections()
        return self._shortest_distance_per_site

    @property
    def connections_flattened(self):
        if self.connections is None:
            self.compute_connections()
        return self._connections_flattened

    @property
    def radius_values(self):
        if self.connections is None:
            self.compute_connections()
        return self._radius_values_per_element

    @property
    def radius_sum_data(self):
        if self.connections is None:
            self.compute_connections()
        return self._radius_sum_per_bond

    @property
    def CN_max_gap_per_site(self):
        if self.connections is None:
            self.compute_connections()
        return self._CN_max_gap_per_site

    @property
    def best_CN_method(self):
        if self.connections is None:
            self.compute_connections()
        return self._best_CN_polyhedrons

    @property
    def CN_connections_by_min_dist_method(self):
        if self.connections is None:
            self.compute_connections()
        return self._CN_connections_by_min_dist_method

    @property
    def CN_connections_by_best_method(self):
        if self.connections is None:
            self.compute_connections()
        return self._CN_connections_by_best_method
