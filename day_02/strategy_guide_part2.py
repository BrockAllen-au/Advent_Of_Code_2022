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

x = lose round
y = draw round
z = win round

"""
from strategy_guide import determine_result

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
            if you == "X":
                required_result = "lose"
            elif you == "Y":
                required_result = "draw"
            else:
                required_result = "win"
            play = determine_play(opponent, required_result)
            total_points += determine_result(opponent, play)
            if play == "X":
                total_points += X
            elif play == "Y":
                total_points += Y
            else:
                total_points += Z
    print(f"Total points: {total_points}")


def determine_play(opponent_play, required_result):
    if opponent_play == "A":
        if required_result == "win":
            play = "Y"
        elif required_result == "draw":
            play = "X"
        else:
            play = "Z"
    if opponent_play == "B":
        if required_result == "win":
            play = "Z"
        elif required_result == "draw":
            play = "Y"
        else:
            play = "X"
    if opponent_play == "C":
        if required_result == "win":
            play = "X"
        elif required_result == "draw":
            play = "Z"
        else:
            play = "Y"
    return play


if __name__ == "__main__":
    main()
