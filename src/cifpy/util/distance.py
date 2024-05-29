import numpy as np


def calculate_cart_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points
    in Cartesian coordinates.
    """
    point1 = np.array(point1)
    point2 = np.array(point2)
    diff = point2 - point1
    distance = np.linalg.norm(diff)

    return distance


def calc_dist_two_cart_points(point1, point2):
    """
    Calculate the Euclidean distance between two points
    in Cartesian coordinates.
    """
    point1 = np.array(point1)
    point2 = np.array(point2)
    diff = point2 - point1
    distance = np.linalg.norm(diff)

    return distance
