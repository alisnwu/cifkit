import logging


def log_conneted_points(all_labels_connections):
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


def log_save_file_message(file_type: str, file_path: str):
    logging.info(f"{file_type} has been saved in {file_path}.")
