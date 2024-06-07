from cifpy.preprocessors.supercell import get_supercell_points
from cifpy.preprocessors.supercell_util import get_cell_atom_count
from cifpy.preprocessors import environment
from cifpy.utils import prompt, folder
from cifpy.models.cif import Cif
import os
import shutil


class CifEnsemble:
    def __init__(self, cif_folder_path: str) -> None:
        self.cif_folder_path = cif_folder_path
        self.cifs: list[Cif] = []
        file_paths = folder.get_file_path_list(cif_folder_path)
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

    @property
    def minimum_distances(self) -> list[tuple[str, float]]:
        """Get a list of tuples containing the file path and the shortest pair distance for each file."""
        return self._collect_cif_data("shortest_pair_distance")

    @property
    def supercell_atom_counts(self) -> list[tuple[str, int]]:
        """Get a list of tuples containing the file path and supercell point counts for each file."""
        return self._collect_cif_data("supercell_points", len)

    # def _moves_cifs_by_attribute(self, attribute: str, value) -> list[str]:
    #     """Return a list of file paths with the matching attribute."""
    #     matching_file_paths = [
    #         cif.file_path
    #         for cif in self.cifs
    #         if getattr(cif, attribute, None) == value
    #     ]

    # def move_files_by_formula(self, formula: str) -> list[str]:
    #     """Filter CIFs by formula."""
    #     return self._moves_cifs_by_attribute("formula", formula)

    # def move_files_by_structure(self, structure: str) -> list[str]:
    #     """Filter CIFs by structure."""
    #     return self._moves_cifs_by_attribute("structure", structure)

    # def move_files_by_elements(self, elements: list[str]) -> list[str]:
    #     """Filter CIFs by elements (assuming unique_elements is a set)."""
    #     filtered_files = []
    #     for cif in self.cifs:
    #         unique_elements: set[str] = getattr(cif, "unique_elements", set())
    #         if set(elements).issubset(unique_elements):
    #             filtered_files.append(cif.file_path)
    #     return filtered_files

    # def move_files_by_space_group_name(self, name: str) -> list[str]:
    #     """Filter CIFs by space group name."""
    #     return self._moves_cifs_by_attribute("space_group_name", name)

    # def move_files_by_space_group_number(self, number: int) -> list[str]:
    #     """Filter CIFs by space group number."""
    #     return self._moves_cifs_by_attribute("space_group_number", number)
