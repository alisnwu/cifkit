# points = np.array(
#     [
#         [0.0, 0.0, 3.881],
#         [0.0, 0.0, 0.0],
#         [3.738, 2.158, 1.94],
#         [3.738, -2.158, 1.94],
#         [4.43, 0.0, 0.0],
#         [4.43, 0.0, 3.881],
#         [-0.936, 1.622, 1.94],
#         [-0.936, -1.622, 1.94],
#         [1.523, 2.638, 0.0],
#         [1.523, -2.638, 0.0],
#         [1.523, -2.638, 3.881],
#         [1.523, 2.638, 3.881],
#         [1.873, 0.0, -1.94],
#         [1.873, 0.0, 5.821],
#         [1.873, 0.0, 1.94],
#     ]
# )

# labels = [
#     "Rh2",
#     "Rh2",
#     "Rh1",
#     "Rh1",
#     "U1",
#     "U1",
#     "In1",
#     "In1",
#     "U1",
#     "U1",
#     "U1",
#     "U1",
#     "In1",
#     "In1",
#     "In1",
# ]


# colors = (
#     generate_contrasting_colors()
# )  # or generate_color_palette_from_colormaps(len(labels))

# label_colors = {label: color for label, color in zip(labels, colors)}


# plotter = pv.Plotter(window_size=(1600, 1200))

# central_atom_index = np.argmin(np.linalg.norm(points, axis=1))
# central_atom = points[central_atom_index]

# for idx, (point, label) in enumerate(zip(points, labels)):
#     radius = (
#         0.4 if np.array_equal(point, central_atom) else 0.4
#     )  # Central atom larger
#     sphere = pv.Sphere(radius=radius, center=point)
#     plotter.add_mesh(sphere, color=label_colors[label])

#     # Add labels with index
#     indexed_label = f"{idx + 1}. {label}"  # Creating a label with numbering
#     adjusted_point = point + [
#         0.3,
#         0.3,
#         0.3,
#     ]  # Offset to avoid overlapping with the sphere
#     if idx != len(points) - 1:
#         plotter.add_point_labels(
#             adjusted_point,
#             [indexed_label],  # Use the indexed label
#             font_size=50,
#             text_color=label_colors[label],
#             always_visible=True,
#             shape=None,
#             margin=0,
#             reset_camera=False,
#         )


# delaunay = Delaunay(points)
# hull = ConvexHull(points)

# edges = set()
# for simplex in delaunay.simplices:
#     for i in range(4):
#         for j in range(i + 1, 4):
#             edge = tuple(sorted([simplex[i], simplex[j]]))
#             edges.add(edge)

# hull_edges = set()
# for simplex in hull.simplices:
#     for i in range(len(simplex)):
#         for j in range(i + 1, len(simplex)):
#             hull_edge = tuple(sorted([simplex[i], simplex[j]]))
#             hull_edges.add(hull_edge)

# for edge in edges:
#     if edge in hull_edges:
#         start, end = points[edge[0]], points[edge[1]]
#         cylinder = pv.Cylinder(
#             center=(start + end) / 2,
#             direction=end - start,
#             radius=0.05,
#             height=np.linalg.norm(end - start),
#         )
#         plotter.add_mesh(cylinder, color="grey")

# faces = []
# for simplex in hull.simplices:
#     faces.append([3] + list(simplex))
# poly_data = pv.PolyData(points, faces)

# plotter.add_mesh(poly_data, color="aqua", opacity=0.3, show_edges=True)

# plotter.show()
