import csv

TOWER_FILE = "input.csv"
MOVE_FILE = "moves.txt"
AMOUNT = 1
STACK_FROM = 3
STACK_TO = 5


def main():
    towers = load_towers(TOWER_FILE)
    print(towers)
    for tower in towers.values():
        tower.reverse()  # Reverse list to replicate stack to have final index as the last item in list
    print(towers)
    process_instructions(towers, MOVE_FILE)
    print()
    print("Crates on top:")
    for key, value in towers.items():
        print(key, value[-1])


def process_instructions(towers, file):
    with open(file) as in_file:
        for line in in_file:
            instruction = line.strip().split()
            move_amount = int(instruction[AMOUNT])
            move_from = int(instruction[STACK_FROM])
            move_to = int(instruction[STACK_TO])
            for i in range(move_amount):
                crate = towers[move_from].pop()
                towers[move_to].append(crate)


def load_towers(file):
    lines = []
    crates = {}
    with open(file) as in_file:
        csv_reader = csv.reader(in_file)
        for row in csv_reader:
            lines.append(row)
    last_line = lines.pop()[0].split()
    for number in last_line:
        crates[int(number)] = []
    for line in lines:
        for i, character in enumerate(line[0]):
            if character == "[":
                crates[(int(i / 4) + 1)].append(line[0][i:i + 3])
            else:
                continue
    return crates


if __name__ == "__main__":
    main()
