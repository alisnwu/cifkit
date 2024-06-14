# import numpy as np
# from functools import partial
# from scipy.optimize import minimize
# from cifpy.data.radius import get_radius_data


# def objective(params, original_radii):
#     return np.sum(((original_radii - params) / original_radii) ** 2)


# def constraint(params, index_pair, shortest_distance):
#     i, j = index_pair
#     return shortest_distance - (params[i] + params[j])


# def optimize_CIF_radii(atom_labels, shortest_distances):
#     radii_data = get_radius_data()
#     original_radii = np.array(
#         [radii_data[label]["CIF_radius"] for label in atom_labels]
#     )
#     atom_labels = atom_labels
#     num_of_elements = len(atom_labels)
#     if num_of_elements == 3:
#         label_to_pair = {"RM": ("In", "Rh"), "MX": ("Rh", "U")}

#     # Constraints setup
#     constraints = []
#     for label, pair in label_to_pair.items():
#         dist = shortest_distances[pair]
#         print(
#             f"Setting constraint for {label} ({pair[0]}-{pair[1]}) with distance {dist}"
#         )
#         i, j = atom_labels.index(pair[0]), atom_labels.index(pair[1])
#         constraints.append(
#             {
#                 "type": "eq",
#                 "fun": partial(
#                     constraint, index_pair=(i, j), shortest_distance=dist
#                 ),
#             }
#         )

#     result = minimize(
#         objective,
#         original_radii,
#         args=(original_radii,),
#         constraints=constraints,
#         options={"disp": True},
#     )

#     if result.success:
#         print("Optimization succeeded.")
#     else:
#         print("Optimization failed:", result.message)

#     return dict(zip(atom_labels, result.x)), result.fun
