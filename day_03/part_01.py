ALPHABET_LOWER = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]
ALPHABET_UPPER = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z"
]

FILE = "rucksacks.txt"


def main():
    with open(FILE) as in_file:
        total_priority = 0
        for line in in_file:
            compartment_01 = line.strip()[:int(len(line) / 2)]
            compartment_02 = line.strip()[int(len(line) / 2):]
            duplicated_letter = extract_duplicate(compartment_01, compartment_02)
            if duplicated_letter in ALPHABET_LOWER:
                total_priority += ALPHABET_LOWER.index(duplicated_letter) + 1
            elif duplicated_letter in ALPHABET_UPPER:
                total_priority += ALPHABET_UPPER.index(duplicated_letter) + 27
    print(f"Total priority = {total_priority}")


def extract_duplicate(compartment_01, compartment_02):
    for letter in compartment_01:
        if letter in compartment_02:
            return letter


if __name__ == "__main__":
    main()
