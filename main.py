import numpy as np

BLOCK = "Block"
BEEHIVE = "Beehive"
LOAF = "Loaf"
BOAT = "Boat"
TUB = "Tub"
BLINKER = "Blinker"
TOAD = "Toad"
BEACON = "Beacon"
GLIDER = "Glider"
LW_SHIP = "LW Spaceship"

PATTERNS = {
    BLOCK: [np.array([[0, 0, 0, 0],
                      [0, 1, 1, 0],
                      [0, 1, 1, 0],
                      [0, 0, 0, 0]])],
    BEEHIVE: [np.array([[0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 0, 0],
                        [0, 1, 0, 0, 1, 0],
                        [0, 0, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0]])],
    LOAF: [np.array([[0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 0, 0],
                     [0, 1, 0, 0, 1, 0],
                     [0, 0, 1, 0, 1, 0],
                     [0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0]])],
    BOAT: [np.array([[0, 0, 0, 0, 0],
                     [0, 1, 1, 0, 0],
                     [0, 1, 0, 1, 0],
                     [0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0]])],
    TUB: [np.array([[0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0]])],
    BLINKER: [np.array([[0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0]]),
              np.array([[0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 1, 1, 1, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0]])],
    TOAD: [np.array([[0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0],
                     [0, 1, 0, 0, 1, 0],
                     [0, 1, 0, 0, 1, 0],
                     [0, 0, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0]]),
           np.array([[0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 1, 0],
                     [0, 1, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0]])],
    BEACON: [np.array([[0, 0, 0, 0, 0, 0],
                       [0, 1, 1, 0, 0, 0],
                       [0, 1, 1, 0, 0, 0],
                       [0, 0, 0, 1, 1, 0],
                       [0, 0, 0, 1, 1, 0],
                       [0, 0, 0, 0, 0, 0]]),
             np.array([[0, 0, 0, 0, 0, 0],
                       [0, 1, 1, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 1, 1, 0],
                       [0, 0, 0, 0, 0, 0]])],
    GLIDER: [np.array([[0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0],
                       [0, 0, 0, 1, 0],
                       [0, 1, 1, 1, 0],
                       [0, 0, 0, 0, 0]]),
             np.array([[0, 0, 0, 0, 0],
                       [0, 1, 0, 1, 0],
                       [0, 0, 1, 1, 0],
                       [0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0]]),
             np.array([[0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 0],
                       [0, 1, 0, 1, 0],
                       [0, 0, 1, 1, 0],
                       [0, 0, 0, 0, 0]]),
             np.array([[0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0],
                       [0, 0, 1, 1, 0],
                       [0, 1, 1, 0, 0],
                       [0, 0, 0, 0, 0]])
             ],
    LW_SHIP: [np.array([[0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0],
                        [0, 1, 0, 0, 0, 1, 0],
                        [0, 0, 1, 1, 1, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0]]),
              np.array([[0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 1, 0, 0],
                        [0, 1, 1, 0, 1, 1, 0],
                        [0, 1, 1, 1, 1, 0, 0],
                        [0, 0, 1, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]]),
              np.array([[0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 1, 1, 0],
                        [0, 1, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 1, 0],
                        [0, 1, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]]),
              np.array([[0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 0, 0, 0],
                        [0, 1, 1, 1, 1, 0, 0],
                        [0, 1, 1, 0, 1, 1, 0],
                        [0, 0, 0, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]])
              ]
}


def count_patterns(grid):
    counts = {}
    width, height = grid.shape
    for pattern in PATTERNS:
        count = 0
        for p in PATTERNS.get(pattern):
            w, h = p.shape
            for i in range(width - w + 1):
                for j in range(height - h + 1):
                    if np.all(grid[i:i + w, j:j + h] == p):
                        count += 1
        counts[pattern] = count
    return counts


def print_pattern_counts(iteration, pattern_counts):
    print(f"Iteration: {iteration}")
    print("−" * 35)
    print("|{:^11}|{:^7}|{:^11}|".format("Configuration", "Count", "Percent"))
    print("|" + "-" * 35 + "|")

    total_count = sum(pattern_counts.values())

    for config, count in pattern_counts.items():
        percent = (count / total_count) * 100 if total_count != 0 else 0
        print("|{:^11}|{:^7}|{:^11.2f}|".format(config, count, percent))

    print("|" + "-" * 35 + "|")
    print("|{:^11}|{:^7}|".format("Total", total_count))
    print("−" * 35)


def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        width, height = map(int, lines[0].split())
        generations = int(lines[1])
        live_cells = [
            tuple(map(int, line.split())) for line in lines[2:]
        ]

    return width, height, generations, live_cells


#
# def generate_output_file(iteration, config_counts):
#     with open(f'output_iteration_{iteration}.txt', 'w') as file:
#         file.write(f"Iteration: {iteration}\n")
#         file.write("-" * 35 + "\n")
#         file.write("|{:^11}|{:^7}|{:^11}|\n".format("Configuration", "Count", "Percent"))
#         file.write("|" + "-" * 35 + "|\n")
#
#         total_count = sum(config_counts.values())
#
#         for config, count in config_counts.items():
#             percent = (count / total_count) * 100 if total_count != 0 else 0
#             file.write("|{:^11}|{:^7}|{:^11.2f}|\n".format(config, count, percent))
#
#         file.write("|" + "-" * 35 + "|\n")
#         file.write("|{:^11}|{:^7}|\n".format("Total", total_count))
#         file.write("−" * 35 + "\n")


def update_grid(grid):
    new_grid = grid.copy()

    for i in range(1, grid.shape[0] - 1):
        for j in range(1, grid.shape[1] - 1):
            neighborhood = grid[i - 1:i + 2, j - 1:j + 2].flatten()
            live_neighbors = np.sum(neighborhood) - grid[i, j]

            if grid[i, j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[i, j] = 0
            else:
                if live_neighbors == 3:
                    new_grid[i, j] = 1

    return new_grid


def main():
    width, height, generations, live_cells = read_input_file("3.in")

    # grid = np.zeros((height + 2, width + 2), dtype=int)
    grid = np.zeros((height, width), dtype=int)

    for cell in live_cells:
        grid[cell[1], cell[0]] = 1

    for iteration in range(1, generations + 1):
        pattern_counts = count_patterns(grid)
        print_pattern_counts(iteration, pattern_counts)
        # generate_output_file(iteration, config_counts)
        grid = update_grid(grid)


if __name__ == "__main__":
    main()
