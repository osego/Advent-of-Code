from collections.abc import Iterable


def parse_input() -> Iterable[int]:
    with open("input.txt") as file:
        input_str = file.read()
    return map(int, input_str.replace("R", "").replace("L", "-").split())


def hundreds_distance(x: int, y: int) -> int:
    if y < 0:
        return (x - 1) // 100 - (x + y - 1) // 100
    else:
        return (x + y) // 100 - x // 100


def main() -> tuple[int, int]:
    part_one = 0
    part_two = 0

    counter = 50

    operations = parse_input()
    for op in operations:
        part_two += hundreds_distance(counter, op)

        counter += op
        if counter % 100 == 0:
            part_one += 1

    return part_one, part_two


if __name__ == "__main__":
    print(main())
