"""
Histgoram for supercell size, minimum distances
"""

import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from cifpy.utils import folder, prompt


def plot_histograms(cif_ensemble, output_dir=None) -> None:

    histograms = [
        {
            "data": cif_ensemble.structures_stats,
            "settings": {
                "file_name": "structures.png",
                "title": "Structures Distribution",
                "xlabel": "Structure",
            },
        },
        {
            "data": cif_ensemble.formula_stats,
            "settings": {
                "file_name": "formula.png",
                "title": "Formulas Distribution",
                "xlabel": "Formula",
            },
        },
        {
            "data": cif_ensemble.tag_stats,
            "settings": {
                "file_name": "tag.png",
                "title": "Tags Distribution",
                "xlabel": "Tag",
            },
        },
        {
            "data": cif_ensemble.space_group_number_stats,
            "settings": {
                "file_name": "space_group_number.png",
                "title": "Space Group Numbers Distribution",
                "xlabel": "Space Group Number",
            },
        },
        {
            "data": cif_ensemble.space_group_name_stats,
            "settings": {
                "file_name": "space_group_name.png",
                "title": "Space Group Names Distribution",
                "xlabel": "Space Group Name",
            },
        },
        {
            "data": cif_ensemble.supercell_size_stats,
            "settings": {
                "file_name": "supercell_size.png",
                "title": "Supercell Sizes Distribution",
                "xlabel": "Supercell Size",
            },
        },
        {
            "data": cif_ensemble.min_distance_stats,
            "settings": {
                "file_name": "min_distance.png",
                "title": "Minimum Distances Distribution",
                "xlabel": "Minimum Distance",
            },
        },
        {
            "data": cif_ensemble.unique_elements_stats,
            "settings": {
                "file_name": "unique_elements.png",
                "title": "Unique Elements Distribution",
                "xlabel": "Element",
            },
        },
    ]

    # Make a deafult folder if the output folder is not provided=
    if not output_dir:
        output_dir = folder.make_output_folder(
            cif_ensemble.dir_path, "histograms"
        )

    for histogram in histograms:
        generate_histogram(
            histogram["data"], histogram["settings"], output_dir
        )


def generate_histogram(data: dict, settings: dict, output_dir: str) -> None:
    """
    Generate a histogram from a dictionary of data and save
    it to a specified directory.
    """
    keys = list(data.keys())
    values = [int(value) for value in data.values()]
    plt.figure(figsize=(10, 6))
    plt.bar(
        keys,
        values,
        color=settings.get("color", "blue"),
        edgecolor=settings.get("edgecolor", "black"),
    )
    plt.title(settings["title"])
    plt.xlabel(settings["xlabel"])
    plt.ylabel("Count")
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
    plt.xticks(rotation=settings.get("rotation", 45), ha="right")
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.tight_layout()

    # File name
    output_file_path = folder.get_file_path(output_dir, settings["file_name"])

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    plt.savefig(output_file_path, dpi=300)
    plt.close()
    prompt.log_save_file_message("Histograms", output_file_path)