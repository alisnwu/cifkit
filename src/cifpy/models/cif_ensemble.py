from cifpy.preprocessors.supercell import get_supercell_points
from cifpy.preprocessors.supercell_util import get_cell_atom_count
from cifpy.preprocessors import environment
from cifpy.utils import prompt, folder
from cifpy.models.cif import Cif


class CifEnsemble:
    def __init__(self, cif_folder_path: str) -> None:
        self.cif_folder_path = cif_folder_path
        self.cifs: list[Cif] = []
        file_paths = folder.get_file_path_list(cif_folder_path)
        self.cifs = [Cif(file_path) for file_path in file_paths]

    """
    Move files on based
    1) tags 2) sgroup 3) sgname 4) supercell size 5) elements 6) structure 7) formula
    """

    def _get_unique_property_values(self, property_name: str):
        """Helper method to fetch unique values for a given property from all Cif objects."""
        return set(
            getattr(cif, property_name)
            for cif in self.cifs
            if hasattr(cif, property_name)
        )

    def get_unique_formulas(self) -> set[str]:
        """Get unique formulas from all .cif files in the folder."""
        return self._get_unique_property_values("formula")

    def get_unique_structures(self) -> set[str]:
        """Get unique structures from all .cif files in the folder."""
        return self._get_unique_property_values("structure")

    def get_unique_space_group_names(self) -> set[str]:
        """Get unique space groups from all .cif files in the folder."""
        return self._get_unique_property_values("space_group_name")

    def get_unique_space_group_numbers(self) -> set[int]:
        """Get unique space group numbers from all .cif files in the folder."""
        return self._get_unique_property_values("space_group_number")

    def get_unique_elements(self) -> set[str]:
        """Get unique elements from all .cif files in the folder."""
        all_elements: set[str] = set()
        for cif in self.cifs:
            if hasattr(cif, "unique_elements"):
                all_elements.update(cif.unique_elements)
        return all_elements

    # Filter
    def _filter_cifs_by_attribute(self, attribute: str, value) -> list[str]:
        """Return a list of file paths with the matching attribute."""
        return [
            cif.file_path
            for cif in self.cifs
            if getattr(cif, attribute, None) == value
        ]

    def filter_by_formula(self, formula: str) -> list[str]:
        """Filter CIFs by formula."""
        return self._filter_cifs_by_attribute("formula", formula)

    def filter_by_structure(self, structure: str) -> list[str]:
        """Filter CIFs by structure."""
        return self._filter_cifs_by_attribute("structure", structure)

    def filter_by_elements(self, elements: list[str]) -> list[str]:
        """Filter CIFs by elements (assuming unique_elements is a set)."""
        filtered_files = []
        for cif in self.cifs:
            unique_elements: set[str] = getattr(cif, "unique_elements", set())
            if set(elements).issubset(unique_elements):
                filtered_files.append(cif.file_path)
        return filtered_files

    def filter_by_space_group_name(self, name: str) -> list[str]:
        """Filter CIFs by space group name."""
        return self._filter_cifs_by_attribute("space_group_name", name)

    def filter_by_space_group_number(self, number: int) -> list[str]:
        """Filter CIFs by space group number."""
        return self._filter_cifs_by_attribute("space_group_number", number)
