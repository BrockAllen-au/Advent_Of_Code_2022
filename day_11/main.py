import re
from monkey import Monkey

FILE = "input"
ROUNDS = 20


def main():
    monkeys = load_monkeys()
    for monkey_round in range(ROUNDS):
        throw_items(monkeys)
    top_inspections = get_top_inspections(monkeys)

    for monkey in monkeys:
        print(f"{monkey.name.title()}: {monkey.items}")
        print(f"{monkey.name.title()}: inspected items {monkey.inspection_count} times.")
    print(top_inspections)
    monkey_business = 1
    for number in top_inspections:
        monkey_business = monkey_business * number
    print(f"Monkey business: {monkey_business}")


def get_top_inspections(monkeys):
    top_inspections = [0, 0]
    for monkey in monkeys:
        if monkey.inspection_count > min(top_inspections):
            top_inspections[top_inspections.index(min(top_inspections))] = monkey.inspection_count
    return top_inspections


def throw_items(monkeys):
    for monkey in monkeys:
        items_to_throw = len(monkey.items)
        for item in monkey.items:
            worry_level = monkey.calculate_worry(item)
            throw_to_monkey = monkey.test_item(worry_level)
            # print(f"{monkey.name} - Throwing item {worry_level} to monkey: {throw_to_monkey}")
            monkeys[throw_to_monkey].items.append(worry_level)
            monkey.inspection_count += 1
        del monkey.items[:items_to_throw]


def load_monkeys():
    monkeys = []
    with open(FILE) as in_file:
        for line in in_file:
            part = line.strip()
            if part.startswith("Monkey"):
                monkey_name = "_".join(part[:-1].split()).lower()
                monkey = Monkey(monkey_name)
                monkeys.append(monkey)
            if part.startswith("Starting"):
                starting_items = []
                parts = re.split('[:,]', part)
                for part in parts:
                    try:
                        starting_items.append(int(part))
                    except ValueError:
                        pass
                monkey.add_items(starting_items)
            if part.startswith("Operation"):
                sections = part.split("=")
                section = sections[1].split()
                monkey.operation = section[1]
                if section[2] == "old":
                    monkey.operation_amount = "old"
                else:
                    monkey.operation_amount = int(section[2])
            if part.startswith("Test:"):
                sections = part.split()
                monkey.test_amount = int(sections[-1])
            if part.startswith("If true:"):
                sections = part.split()
                monkey.throw_true = int(sections[-1])
            if part.startswith("If false:"):
                monkey.throw_false = int(part.split()[-1])
    return monkeys


if __name__ == "__main__":
    main()
