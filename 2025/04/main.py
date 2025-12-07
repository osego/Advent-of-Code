def parse_input(file_path: str) -> list[list[int]]:
    with open(file_path) as file:
        input_str = file.read()
    return [list(map(lambda chracter: int(chracter == "@"), line)) for line in input_str.strip().splitlines()]


def get_neighbors(grid: list[list[int]], x: int, y: int) -> list[int]:
    neighbors = []
    for x_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            if (
                (x_offset == 0 and y_offset == 0)
                or (y + y_offset) < 0
                or (y + y_offset) > len(grid) - 1
                or (x + x_offset) < 0
                or (x + x_offset) > len(grid[0]) - 1
            ):
                continue
            neighbors.append(grid[y + y_offset][x + x_offset])
    return neighbors


def part_one(file_path: str) -> int:
    grid = parse_input(file_path)
    total = 0

    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if not value:
                continue
            if sum(get_neighbors(grid, x, y)) < 4:
                total += 1

    return total


def part_two(file_path: str) -> int:
    grid = parse_input(file_path)
    total = 0
    to_remove: list[tuple[int, int]] = []

    while True:
        for y, row in enumerate(grid):
            for x, value in enumerate(row):
                if not value:
                    continue
                if sum(get_neighbors(grid, x, y)) < 4:
                    total += 1
                    to_remove.append((x, y))

        if not to_remove:
            break
        for x, y in to_remove:
            grid[y][x] = 0
        to_remove = []

    return total


if __name__ == "__main__":
    input_file_path = "input.txt"
    print(part_one(input_file_path))
    print(part_two(input_file_path))
