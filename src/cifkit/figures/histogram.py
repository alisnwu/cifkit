"""
Histgoram for supercell size, minimum distances
"""

import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from cifkit.utils import folder, prompt


def plot_histogram(attribute, stats, dir_path, display, output_dir):
    if not output_dir:
        output_dir = folder.make_output_folder(dir_path, "histograms")

    if attribute == "structure":
        histogram = {
            "data": stats,
            "settings": {
                "file_name": "structures.png",
                "title": "Structures Distribution",
                "xlabel": "Structure",
            },
        }

    if attribute == "formula":
        histogram = {
            "data": stats,
            "settings": {
                "file_name": "formula.png",
                "title": "Formulas Distribution",
                "xlabel": "Formula",
            },
        }

    if attribute == "tag":
        histogram = {
            "data": stats,
            "settings": {
                "file_name": "tag.png",
                "title": "Tags Distribution",
                "xlabel": "Tag",
            },
        }

    if attribute == "space_group_number":
        histogram = {
            "data": stats,
            "settings": {
                "file_name": "space_group_number.png",
                "title": "Space Group Numbers Distribution",
                "xlabel": "Space Group Number",
            },
        }

    if attribute == "space_group_name":
        histogram = {
            "data": stats,
            "settings": {
                "file_name": "space_group_name.png",
                "title": "Space Group Names Distribution",
                "xlabel": "Space Group Name",
            },
        }

    if attribute == "supercell_size":
        histogram = {
            "data": stats,
            "settings": {
                "file_name": "supercell_size.png",
                "title": "Supercell Sizes Distribution",
                "xlabel": "Supercell Size",
            },
        }

    if attribute == "min_distance":
        histogram = {
            "data": stats,
            "settings": {
                "file_name": "min_distance.png",
                "title": "Minimum Distances Distribution",
                "xlabel": "Minimum Distance",
                "key_data_type": "float",
            },
        }

    if attribute == "elements":
        histogram = {
            "data": stats,
            "settings": {
                "file_name": "elements.png",
                "title": "Unique Elements Distribution",
                "xlabel": "Element",
            },
        }
    if attribute == "CN_by_min_dist_method":
        histogram = {
            "data": stats,
            "settings": {
                "file_name": "CN_by_min_dist_method.png",
                "title": "Coordination Numbers Distribution by Min Dist Method",
                "xlabel": "Coordination Number",
            },
        }

    if attribute == "CN_by_best_methods":
        histogram = {
            "data": stats,
            "settings": {
                "file_name": "CN_by_best_methods.png",
                "title": "Coordination Numbers Distribution by Best Methods",
                "xlabel": "Coordination Number",
            },
        }

    if attribute == "composition_type":
        histogram = {
            "data": stats,
            "settings": {
                "file_name": "composition_type.png",
                "title": "Unique Composition Types Distribution",
                "xlabel": "Compositions (1: unary, 2: binary, 3: ternary, etc.)",
                "key_data_type": "string",
            },
        }

    if attribute == "site_mixing_type":
        histogram = {
            "data": stats,
            "settings": {
                "file_name": "site_mixing_type.png",
                "title": "Site Mixing Distribution",
                "xlabel": "Site Mixing Type",
            },
        }
    generate_histogram(
        histogram["data"], histogram["settings"], display, output_dir
    )

    # Make a deafult folder if the output folder is not provided=


def generate_histogram(data, settings, display, output_dir: str) -> None:
    """
    Generate a histogram from a dictionary of data and save
    it to a specified directory.
    """

    plt.figure(figsize=(10, 6))  # Create a new figure for each histogram

    if settings.get("key_data_type") == "string":
        # Sorting keys if they are string representations of integers
        data = {str(key): data[key] for key in sorted(data.keys(), key=int)}

    if settings.get("key_data_type") != "float":
        plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

    keys = list(data.keys())
    values = [data[key] for key in keys]

    plt.bar(
        keys,
        values,
        color=settings.get("color", "blue"),
        edgecolor=settings.get("edgecolor", "black"),
    )
    plt.title(settings["title"])
    plt.xlabel(settings["xlabel"])
    plt.ylabel("Count")
    plt.xticks(rotation=settings.get("rotation", 45), ha="right")
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.tight_layout()

    output_file_path = folder.get_file_path(output_dir, settings["file_name"])
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    plt.savefig(output_file_path, dpi=300)
    if display:
        plt.show()  # Display the plot if requested
        plt.close()  # Close the plot after saving and optionally displaying

    prompt.log_save_file_message("Histograms", output_file_path)
