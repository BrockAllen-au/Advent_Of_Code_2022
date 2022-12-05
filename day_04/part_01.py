FILE = "input.txt"


def main():
    with open(FILE) as in_file:
        total = 0
        overlap_total = 0
        for line in in_file:
            parts = (line.strip().replace("-", " ").replace(",", " ").split())
            converted_numbers = []
            for i, part in enumerate(parts):
                converted_numbers.append(int(part))
            number_range_01 = set([number for number in range(converted_numbers[0], converted_numbers[1] + 1)])
            number_range_02 = set([number for number in range(converted_numbers[2], converted_numbers[3] + 1)])
            comparison = set.intersection(number_range_01, number_range_02)
            if comparison == number_range_01 or comparison == number_range_02:
                total += 1
            if comparison != set():
                overlap_total += 1

        print(f"Total full duplication: {total}")
        print(f"Total overlap duplication: {overlap_total}")


if __name__ == "__main__":
    main()
