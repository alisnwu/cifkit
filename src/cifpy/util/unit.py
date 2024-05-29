import numpy as np


def get_radians_from_degrees(angles: list[float]) -> list[float]:
    """
    Converts angles from degrees to radians and round to 5 decimal places.
    """
    radians = [round(np.radians(angle), 5) for angle in angles]
    return radians


def round_float(distance: float, precision: int = 3) -> float:
    """
    Round a distance value to a specified precision.
    """
    return round(distance, precision)
