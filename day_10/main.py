INPUT_FILE = "input"
CYCLE_CHECKS = [20, 60, 100, 140, 180, 220]


def main():
    crt_display = []
    cycle_count = 1
    register = 1
    total_signal_strength = 0
    instructions = load_instructions()
    total_signal_strength = process_instructions(cycle_count, instructions, register, total_signal_strength)
    print("Part 01:")
    print(total_signal_strength)
    print()


def process_instructions(cycle_count, instructions, register, total_signal_strength):
    for instruction in instructions:
        if instruction.startswith("addx"):
            addx_cycle = 2
            while addx_cycle != 0:
                if cycle_count in CYCLE_CHECKS:
                    total_signal_strength += calculate_total_signal_strength(cycle_count, register)
                parts = instruction.split()
                if addx_cycle == 2:
                    cycle_count += 1  # addx does nothing on first cycle
                    addx_cycle -= 1
                else:
                    register += int(parts[1])
                    addx_cycle -= 1
                    cycle_count += 1
        elif cycle_count in CYCLE_CHECKS:
            total_signal_strength += calculate_total_signal_strength(cycle_count, register)
            cycle_count += 1
        else:
            cycle_count += 1  # Count a cycle for a noop command
    return total_signal_strength


def calculate_total_signal_strength(cycle_count, register):
    return register * cycle_count


def load_instructions():
    instructions = []
    with open(INPUT_FILE) as in_file:
        for line in in_file:
            instructions.append(line.strip())
    return instructions


if __name__ == "__main__":
    main()
