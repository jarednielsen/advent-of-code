

def read_input():
    lines = []
    with open("dec06_input.txt", "r") as infile:
        for line in infile:
            lines.append(line)
    return lines

def questions(group):
    chars = set(group.replace(" ", "").replace("\n", ""))
    return len(chars)

def questions2(group):
    lines = group.split("\n")
    chars_intersection = None
    for line in lines:
        if chars_intersection is None:
            chars_intersection = set(line)
        else:
            chars_intersection = chars_intersection.intersection(set(line))
    return len(chars_intersection)


def main(lines):
    groups = "".join(lines).split("\n\n")

    counts = []
    for group in groups:
        counts.append(questions2(group))
    return sum(counts)



if __name__ == "__main__":
    lines = read_input()
    res = main(lines)
    print(res)