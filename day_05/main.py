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
    process_instructions_01(towers, MOVE_FILE)
    print(f"Part 01 Crates:\n")
    display_top_crates(towers)
    towers = load_towers(TOWER_FILE)
    for tower in towers.values():
        tower.reverse()  # Reverse list to replicate stack to have final index as the last item in list
    process_instructions_02(towers, MOVE_FILE)
    print(f"Part 02 Crates:\n")
    display_top_crates(towers)


def display_top_crates(towers):
    print("Crates on top:")
    for key, value in towers.items():
        print(key, value[-1])


def process_instructions_01(towers, instructions):
    with open(instructions) as in_file:
        for line in in_file:
            instruction = line.strip().split()
            move_amount = int(instruction[AMOUNT])
            move_from = int(instruction[STACK_FROM])
            move_to = int(instruction[STACK_TO])
            for i in range(move_amount):
                crate = towers[move_from].pop()
                towers[move_to].append(crate)


def process_instructions_02(towers, instructions):
    with open(instructions) as in_file:
        for line in in_file:
            crates_to_move = []
            instruction = line.strip().split()
            move_amount = int(instruction[AMOUNT])
            move_from = int(instruction[STACK_FROM])
            move_to = int(instruction[STACK_TO])
            for i in range(move_amount):
                crate = towers[move_from].pop()
                crates_to_move.append(crate)
            crates_to_move.reverse()
            for box in crates_to_move:
                towers[move_to].append(box)


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
