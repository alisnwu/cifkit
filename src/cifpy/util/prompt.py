def print_conneted_points(all_labels_connections):
    for label, connections in all_labels_connections.items():
        print(f"\nAtom site {label}:")
        for (
            label,
            dist,
            coords_1,
            coords_2,
            diff,
        ) in connections:
            print(f"{label} {dist} {coords_1}, {coords_2}, {diff}")
    print()
