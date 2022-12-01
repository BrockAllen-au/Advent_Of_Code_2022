FILE = "calories.txt"

elf_count = 1
highest_elf_number = 0
highest_calorie_total = 0


with open(FILE) as in_file:
    calories = []
    for line in in_file:
        line.strip()
        if line == "\n":
            calorie_count = sum(calories)
            if calorie_count > highest_calorie_total:
                highest_elf_number = elf_count
                highest_calorie_total = calorie_count
            calories = []
            elf_count += 1
        else:
            calories.append(int(line))

print(f"Highest elf: {highest_elf_number}, with a total calorie count of: {highest_calorie_total}")
