FILE = "calories.txt"

highest_calorie_total = [0, 0, 0]

with open(FILE) as in_file:
    calories = []
    for line in in_file:
        line.strip()
        if line == "\n":
            calorie_count = sum(calories)
            if calorie_count > min(highest_calorie_total):
                highest_calorie_total[highest_calorie_total.index(min(highest_calorie_total))] = calorie_count
            calories = []
        else:
            calories.append(int(line))

print(highest_calorie_total)
print(sum(highest_calorie_total))
