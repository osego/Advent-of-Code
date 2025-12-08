def parse_input(file_path: str) -> tuple[list[tuple[int, int]], list[int]]:
    with open(file_path) as file:
        input_str = file.read()

    ranges_str, ids_str = input_str.strip().split("\n\n")

    ranges = [tuple(map(int, range_str.split("-"))) for range_str in ranges_str.strip().splitlines()]
    ids = list(map(int, ids_str.strip().splitlines()))

    return ranges, ids


def part_one(file_path: str) -> int:
    range_tuples, ingredients = parse_input(file_path)
    ranges = [range(low, high + 1) for low, high in range_tuples]

    total = 0

    for ingredient in ingredients:
        total += any(ingredient in range_ for range_ in ranges)

    return total


def part_two(file_path: str) -> int:
    input_tuples = sorted(set(parse_input(file_path)[0]))
    result_tuples = [input_tuples[0]]

    for input_range in input_tuples[1:]:
        if input_range[0] - 1 > result_tuples[-1][1]:
            result_tuples.append(input_range)
        else:
            result_tuples[-1] = (result_tuples[-1][0], max(input_range[1], result_tuples[-1][1]))

    ranges = [range(low, high + 1) for low, high in result_tuples]
    return sum(map(len, ranges))


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
