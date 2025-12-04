from collections.abc import Iterable
from functools import partial


def parse_input() -> Iterable[list[int]]:
    with open("input.txt") as file:
        input_str = file.read()
    return map(list, map(partial(map, int), input_str.strip().splitlines()))


def part_one() -> int:
    enabled = 0
    for bank in parse_input():
        tens = max(bank[:-1])
        ones = max(bank[bank.index(tens) + 1 :]) + 1
        enabled += tens * 10 + ones

    return enabled


def highest_digit(bank: list[int], start: int, end: int) -> tuple[int, int]:
    # workaround for getting the last digit - if `end` is 0 (technically, -0) slicing doesn't work
    end = end or None

    digit = max(bank[start:end])
    index = bank[start:end].index(digit) + start + 1
    return (digit, index)


def part_two() -> int:
    total = 0

    position_multipliers = tuple(reversed([10**k for k in range(12)]))

    for bank in parse_input():
        enabled = []
        start = 0
        for i in range(12):
            digit, start = highest_digit(bank, start, -(11 - i))
            enabled.append(digit)
        total += sum(digit * p for digit, p in zip(enabled, position_multipliers, strict=True))

    return total


if __name__ == "__main__":
    print(part_one())
    print(part_two())
