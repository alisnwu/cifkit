import pytest
from cifpy.data.radius import get_radius_data
from cifpy.data.radius_optimization import get_refined_CIF_radii


def get_CIF_pauling_radii(elements: list[str]) -> dict:
    """
    Return CIF and Pualing data for a list of elements
    """
    data = get_radius_data()
    radii = {}
    for atom in elements:
        radii[atom] = {
            "CIF": data[atom]["CIF_radius"],
            "Pauling": data[atom]["Pauling_radius_CN12"],
        }

    return radii


def merge_refined_CIF_radii(elements, shortest_bond_distances) -> dict:

    CIF_pauling_rad = get_CIF_pauling_radii(elements)
    CIF_refined_rad = get_refined_CIF_radii(elements, shortest_bond_distances)

    combined_radii = {}
    for element in elements:
        combined_radii[element] = {
            "CIF_radius": CIF_pauling_rad[element]["CIF"],
            "CIF_radius_refined": CIF_refined_rad.get(element),
            "Pauling_radius_CN12": CIF_pauling_rad[element]["Pauling"],
        }

    return combined_radii


def compute_pair_distances(radii_data):
    # Create a sorted list of element keys (A, B, C, ...)
    elements = sorted(radii_data.keys())
    pair_distances = {
        "CIF_radius_sum": {},
        "CIF_radius_refined_sum": {},
        "Pauling_radius_sum": {},
    }

    # Calculate pair sums for each unique combination of elements
    for i, elem_i in enumerate(elements):
        for j in range(i, len(elements)):
            elem_j = elements[j]

            # Element pair label, e.g., A-B or A-A
            pair_label = (
                f"{elem_i}-{elem_j}" if i != j else f"{elem_i}-{elem_i}"
            )

            # Sum radii for each radius type
            pair_distances["CIF_radius_sum"][pair_label] = round(
                radii_data[elem_i]["CIF_radius"]
                + radii_data[elem_j]["CIF_radius"],
                3,
            )
            pair_distances["CIF_radius_refined_sum"][pair_label] = round(
                radii_data[elem_i]["CIF_radius_refined"]
                + radii_data[elem_j]["CIF_radius_refined"],
                3,
            )
            pair_distances["Pauling_radius_sum"][pair_label] = round(
                radii_data[elem_i]["Pauling_radius_CN12"]
                + radii_data[elem_j]["Pauling_radius_CN12"],
                3,
            )

    return pair_distances
