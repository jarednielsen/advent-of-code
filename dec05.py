

def read_input():
    lines = []
    with open("dec05_input.txt", "r") as infile:
        for line in infile:
            lines.append(line.strip())
    return lines

def to_binary(line):
    binary = line.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0")
    return int(binary, 2)


def main(lines):
    ids = []
    for line in lines:
        seat_id = 8 * to_binary(line[:7]) + to_binary(line[7:10])
        ids.append(seat_id)
    return ids

def find_missing(ids):
    ids_set = set(ids)
    for i in range(54, 890):
        if i not in ids_set:
            print(f"Found missing id: {i}")
            return i


if __name__ == "__main__":
    lines = read_input()
    ids = main(lines)
    print(f"Highest ID: {max(ids)}")
    ids.sort()
    for id in ids:
        print(id)
    find_missing(ids)