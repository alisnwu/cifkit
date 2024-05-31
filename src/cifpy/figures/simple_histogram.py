"""
Histgoram for supercell size, minimum distances
"""

import os
import matplotlib.pyplot as plt
from cifpy.utils import folder, prompt


def generate_histogram(
    data: list[int] | list[float], dir_path: str, settings: dict
) -> None:
    """
    Generate a histogram from a list of numbers and save
    it to a specified directory.
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

    prompt.log_save_file_message("Histogram", output_file_path)
