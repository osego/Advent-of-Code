from collections.abc import Iterable


def parse_input() -> Iterable[int]:
    with open("input.txt") as file:
        input_str = file.read()
    return map(int, input_str.replace("R", "").replace("L", "-").split())


def main() -> int:
    result = 0
    counter = 50

    operations = parse_input()
    for op in operations:
        counter += op
        if counter % 100 == 0:
            result += 1

    return result


if __name__ == "__main__":
    print(main())
