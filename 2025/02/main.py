def parse_input() -> list[tuple[int, int]]:
    with open("input.txt") as file:
        input_str = file.read()

    return [tuple(map(int, range_str.split("-"))) for range_str in input_str.strip().split(",")]


def factorize(n: int) -> list[tuple[int, int]]:
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append((i, n // i))
    return factors


def main() -> tuple[int, int]:
    ranges = parse_input()
    part_one = set()
    part_two = set()

    precomputed_factors = {k: factorize(k) for k in range(1, 10 + 1)}

    for low, high in ranges:
        for string_id in map(str, range(low, high + 1)):
            digit_count = len(string_id)

            if digit_count < 2:
                continue

            if string_id[0 : digit_count // 2] * 2 == string_id:
                part_one.add(string_id)

            for low_factor, high_factor in precomputed_factors[digit_count]:
                if string_id[0:low_factor] * high_factor == string_id or (
                    low_factor != 1 and string_id[0:high_factor] * low_factor == string_id
                ):
                    part_two.add(string_id)
                    break

    return sum(map(int, part_one)), sum(map(int, part_two))


if __name__ == "__main__":
    print(main())
