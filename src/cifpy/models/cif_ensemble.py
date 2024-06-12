from cifpy.models.cif import Cif
from cifpy.utils.folder import move_files, copy_files, get_file_path_list
from cifpy.figures.histogram import plot_histograms
from collections import Counter


class CifEnsemble:
    def __init__(self, cif_dir_path: str) -> None:
        self.dir_path = cif_dir_path
        self.file_paths = get_file_path_list(cif_dir_path)
        self.file_count = len(self.file_paths)
        self.cifs = [Cif(file_path) for file_path in self.file_paths]

    def _get_unique_property_values(self, property_name: str):
        """Return unique values for a given property from cifs."""
        return set(
            getattr(cif, property_name)
            for cif in self.cifs
            if hasattr(cif, property_name)
        )

    @property
    def unique_formulas(self) -> set[str]:
        """Get unique formulas from all .cif files in the folder."""
        return self._get_unique_property_values("formula")

    @property
    def unique_structures(self) -> set[str]:
        """Get unique structures from all .cif files in the folder."""
        return self._get_unique_property_values("structure")

    @property
    def unique_tags(self) -> set[str]:
        """Get unique formulas from all .cif files in the folder."""
        return self._get_unique_property_values("tag")

    @property
    def unique_space_group_names(self) -> set[str]:
        """Get unique space groups from all .cif files in the folder."""
        return self._get_unique_property_values("space_group_name")

    @property
    def unique_space_group_numbers(self) -> set[int]:
        """Get unique space group numbers from all .cif files in the folder."""
        return self._get_unique_property_values("space_group_number")

    @property
    def unique_site_mixing_types(self) -> set[int]:
        """Get unique site mixing types from all .cif files in the folder."""
        return self._get_unique_property_values("site_mixing_type")

    def _get_unique_property_values_from_set(self, property_name: str):
        unique_values = set()
        for cif in self.cifs:
            unique_values.update(getattr(cif, property_name))
        return unique_values

    @property
    def unique_elements(self) -> set[str]:
        """Get unique elements from all .cif files in the folder."""
        return self._get_unique_property_values_from_set("unique_elements")

    @property
    def unique_coordination_numbers(self) -> set[str]:
        """Get unique elements from all .cif files in the folder."""
        return self._get_unique_property_values_from_set(
            "unique_coordination_numbers"
        )

    def _attribute_stats(self, attribute_name, transform=None):
        """
        Helper method to compute the count of each unique value of a given
        attribute across all Cif objects.
        """
        values = [
            (
                transform(getattr(cif, attribute_name))
                if transform
                else getattr(cif, attribute_name)
            )
            for cif in self.cifs
            if hasattr(cif, attribute_name)
        ]
        # Flatten the list if the attribute is a set of elements
        if isinstance(values[0], set):
            values = [elem for sublist in values for elem in sublist]
        return dict(Counter(values))

    @property
    def structures_stats(self) -> dict[str, int]:
        return self._attribute_stats("structure")

    @property
    def formula_stats(self) -> dict[str, int]:
        return self._attribute_stats("formula")

    @property
    def tag_stats(self) -> dict[str, int]:
        return self._attribute_stats("tag")

    @property
    def space_group_number_stats(self) -> dict[str, int]:
        return self._attribute_stats("space_group_number")

    @property
    def space_group_name_stats(self) -> dict[str, int]:
        return self._attribute_stats("space_group_name")

    @property
    def unique_elements_stats(self) -> dict[str, int]:
        """Sum the counts of each unique element"""
        return self._attribute_stats("unique_elements")

    @property
    def supercell_size_stats(self) -> dict[int, int]:
        return self._attribute_stats("supercell_points", len)

    @property
    def min_distance_stats(self) -> dict[float, int]:
        return self._attribute_stats("shortest_pair_distance")

    @property
    def unique_coordination_numbers_stats(self) -> dict[float, int]:
        return self._attribute_stats("unique_coordination_numbers")

    def _collect_cif_data(self, attribute, transform=None):
        """Generic method to collect data from CIF files based on an attribute."""
        collected_data = []
        for cif in self.cifs:
            attr_value = getattr(cif, attribute, None)
            if attr_value is not None:
                if transform:
                    value = transform(attr_value)
                else:
                    value = attr_value
                collected_data.append((cif.file_path, value))
            else:
                print(f"No valid {attribute} for {cif.file_path}")
        return collected_data

    @property
    def minimum_distances(self) -> list[tuple[str, float]]:
        return self._collect_cif_data("shortest_pair_distance")

    @property
    def supercell_atom_counts(self) -> list[tuple[str, int]]:
        return self._collect_cif_data("supercell_atom_count")

    def _filter_by_value(self, property_name: str, values: list):
        cif_file_paths = set()
        for cif in self.cifs:
            property_value = getattr(cif, property_name, None)
            if not isinstance(property_value, set):
                if property_value in values:
                    cif_file_paths.add(cif.file_path)
            else:
                # Handle the case where property_value is a set
                if all(val in property_value for val in values):
                    cif_file_paths.add(cif.file_path)
        return cif_file_paths

    def filter_by_formulas(self, values: list[str]) -> set[str]:
        return self._filter_by_value("formula", values)

    def filter_by_structures(self, values: list[str]) -> set[str]:
        return self._filter_by_value("structure", values)

    def filter_by_elements(self, values: list[str]) -> set[str]:
        return self._filter_by_value("unique_elements", values)

    def filter_by_tags(self, values: list[str]) -> set[str]:
        return self._filter_by_value("tag", values)

    def filter_by_space_group_names(self, values: list[str]) -> set[str]:
        return self._filter_by_value("space_group_name", values)

    def filter_by_space_group_numbers(self, values: list[int]) -> set[str]:
        return self._filter_by_value("space_group_number", values)

    def filter_by_site_mixing_types(self, values: list[str]) -> set[str]:
        return self._filter_by_value("site_mixing_type", values)

    def filter_by_coordination_numbers(self, values: list[int]) -> set[str]:
        return self._filter_by_value("unique_coordination_numbers", values)

    def _filter_by_range(
        self, property: str, min: float | int, max: float | int
    ) -> set[str]:

        cif_file_paths = set()
        for cif in self.cifs:
            property_value = getattr(cif, property, None)
            if property_value is None:
                continue
            if property_value < min or property_value > max:
                continue
            cif_file_paths.add(cif.file_path)
        return cif_file_paths

    def filter_by_min_distance(
        self, min_distance: float, max_distance: float
    ) -> set[str]:
        return self._filter_by_range(
            "shortest_pair_distance", min_distance, max_distance
        )

    def filter_by_supercell_count(
        self, min_count: int, max_count: int
    ) -> set[str]:
        return self._filter_by_range(
            "supercell_atom_count",
            min_count,
            max_count,
        )

    def move_cif_files(
        self, file_paths: set[str], to_directory_path: str
    ) -> None:
        """Move a set of CIF files to a destination directory."""
        move_files(to_directory_path, list(file_paths))

    def copy_cif_files(
        self, file_paths: set[str], to_directory_path: str
    ) -> None:
        """Copy a set of CIF files to a destination directory."""
        copy_files(to_directory_path, list(file_paths))

    """Plot histograms"""

    def generate_stat_histograms(self, output_dir=None):
        plot_histograms(self, output_dir)
