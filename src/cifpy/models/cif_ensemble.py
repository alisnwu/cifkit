from cifpy.preprocessors.supercell import get_supercell_points
from cifpy.preprocessors.supercell_util import get_cell_atom_count
from cifpy.preprocessors import environment
from cifpy.utils import prompt
from cifpy.utils.folder import move_files, copy_files, get_file_path_list
from cifpy.models.cif import Cif
import os
import shutil


class CifEnsemble:
    def __init__(self, cif_folder_path: str) -> None:
        self.cif_folder_path = cif_folder_path
        self.cifs: list[Cif] = []
        file_paths = get_file_path_list(cif_folder_path)
        self.cifs = [Cif(file_path) for file_path in file_paths]

    def _get_unique_property_values(self, property_name: str):
        """Helper method to et unique values for a given property from cifs."""
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
    def unique_elements(self) -> set[str]:
        """Get unique elements from all .cif files in the folder."""
        all_elements = set()
        for cif in self.cifs:
            if hasattr(cif, "unique_elements"):
                all_elements.update(cif.unique_elements)
        return all_elements

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

    def _filter_cif_data(self, property_name: str, values: list):
        cif_file_paths = set()
        for cif in self.cifs:
            property_value = getattr(cif, property_name, None)
            if not isinstance(property_value, set):
                if property_value in values:
                    print(property_name, property_value)
                    cif_file_paths.add(cif.file_path)
            else:
                # Handle the case where property_value is a set
                if all(val in property_value for val in values):
                    cif_file_paths.add(cif.file_path)
        return cif_file_paths

    @property
    def minimum_distances(self) -> list[tuple[str, float]]:
        """
        Get a list of tuples containing the file path and the shortest pair
        istance for each file.
        """
        return self._collect_cif_data("shortest_pair_distance")

    @property
    def supercell_atom_counts(self) -> list[tuple[str, int]]:
        """
        Get a list of tuples containing the file path and supercell point
        counts for each file.
        """
        return self._collect_cif_data("supercell_points", len)

    def filter_by_formulas(self, values: list[str]) -> set[str]:
        return self._filter_cif_data("formula", values)

    def filter_by_structures(self, values: list[str]) -> set[str]:
        return self._filter_cif_data("structure", values)

    def filter_by_elements(self, values: list[str]) -> set[str]:
        return self._filter_cif_data("unique_elements", values)

    def filter_by_tags(self, values: list[str]) -> set[str]:
        return self._filter_cif_data("tag", values)

    def filter_by_space_group_names(self, values: list[str]) -> set[str]:
        return self._filter_cif_data("space_group_name", values)

    def filter_by_space_group_numbers(self, values: list[str]) -> set[str]:
        return self._filter_cif_data("space_group_number", values)

    def move_cif_files(
        self, file_paths: set[str], to_directory_path: str
    ) -> None:
        """
        Move a set of CIF files to a specified destination directory.
        """
        move_files(to_directory_path, list(file_paths))

    def copy_cif_files(
        self, file_paths: set[str], to_directory_path: str
    ) -> None:
        """
        Copy a set of CIF files to a specified destination directory.
        """
        copy_files(to_directory_path, list(file_paths))

    # Let's format all the cif objects
