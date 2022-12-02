"""
A = Rock
B = Paper
C = Scissors

X = Rock
x > c, x < b, x == a
Y = Paper
y > a, y < c, y == b
Z = Scissors
z > b, z < a, z == c

Win = 6
Draw = 3
Loss = 0
"""

FILE = "strategy_guide.txt"
X = 1
Y = 2
Z = 3
WIN = 6
DRAW = 3
LOSE = 0


def main():
    total_points = 0
    with open(FILE) as in_file:
        for line in in_file:
            opponent = line.strip()[0]
            you = line.strip()[2]
            total_points += determine_result(opponent, you)
            if you == "X":
                total_points += X
            elif you == "Y":
                total_points += Y
            else:
                total_points += Z
    print(f"Total points: {total_points}")


def determine_result(opponent_play, your_play):
    if opponent_play == "A":
        if your_play == "X":
            result = DRAW
        elif your_play == "Y":
            result = WIN
        else:
            result = LOSE
    if opponent_play == "B":
        if your_play == "X":
            result = LOSE
        elif your_play == "Y":
            result = DRAW
        else:
            result = WIN
    if opponent_play == "C":
        if your_play == "X":
            result = WIN
        elif your_play == "Y":
            result = LOSE
        else:
            result = DRAW
    return result


if __name__ == "__main__":
    main()
