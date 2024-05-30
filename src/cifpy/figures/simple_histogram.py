"""
Histgoram for supercell size, minimum distances
"""

import os
import matplotlib.pyplot as plt
from cifpy.utils import folder


def generate_histogram(
    data: list, dir_path: str, settings: dict
) -> None:
    """
    Generates a histogram from the provided data and saves it to a specified directory.

    Parameters:
        data (list): List of data points to plot.
        dir_path (str): Directory path where the histogram will be saved.
        settings (dict): Dictionary containing settings for the plot.
    """
    output_dir_path = folder.make_output_folder(dir_path, "plot")
    output_file_path = folder.get_file_path(
        output_dir_path, settings["file_name"]
    )
    plt.figure(figsize=(10, 6))
    plt.hist(
        data,
        bins=settings.get("bins", 50),
        color=settings.get("color", "blue"),
        edgecolor=settings.get("edgecolor", "black"),
    )
    plt.title(settings["title"])
    plt.xlabel(settings["xlabel"])
    plt.ylabel(settings["ylabel"])
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.savefig(output_file_path, dpi=300)
    plt.close()

    print(f"Histogram has been saved in {output_file_path}")
