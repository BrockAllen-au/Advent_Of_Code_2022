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
    elf_groups = []
    duplicates = []
    total = 0
    with open(FILE) as in_file:
        group = []
        count = 0
        for line in in_file:
            group.append(line.strip())
            count += 1
            if count % 3 == 0 and count != 0:
                elf_groups.append(group)
                group = []

    for elfs in elf_groups:
        print(elfs)
        elf_01 = set(elfs[0])
        elf_02 = set(elfs[1])
        elf_03 = set(elfs[2])
        for letter in elf_01:
            if letter in elf_02 and letter in elf_03:
                duplicates.append(letter)
                if letter in ALPHABET_LOWER:
                    total += ALPHABET_LOWER.index(letter) + 1
                elif letter in ALPHABET_UPPER:
                    total += ALPHABET_UPPER.index(letter) + 27

    print(total)


if __name__ == "__main__":
    main()
