FILE = "input.txt"


def main():
    with open(FILE) as in_file:
        text = in_file.read()
        start_marker = []
        process_part01(start_marker, text)
        print("Part 01:", len(start_marker[0]))
        process_part02(start_marker, text)
        print("Part 02:", len(start_marker[0]))


def process_part01(start_marker, text):
    count = 0
    active = True
    while active:
        if count == 0:
            start_marker.append(text[0:count + 4])
            count += 1
            marker = set(start_marker)
        elif len(marker) < 4:
            start_marker[0] = text[0:count + 4]
            last_four = start_marker[0][-4:]
            marker = set(last_four)
            count += 1
        else:
            active = False


def process_part02(start_marker, text):
    count = 0
    active = True
    while active:
        if count == 0:
            start_marker.append(text[0:count + 14])
            count += 1
            marker = set(start_marker)
        elif len(marker) < 14:
            start_marker[0] = text[0:count + 14]
            last_four = start_marker[0][-14:]
            marker = set(last_four)
            count += 1
        else:
            active = False


if __name__ == "__main__":
    main()
