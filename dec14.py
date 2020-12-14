from typing import List

def read_input():
    lines = []
    with open("dec14_input.txt", "r") as infile:
        for line in infile:
            if line:
                lines.append(line.strip())
    return lines

def mask_value(mask: str, value: int):
    binary: str = "{:036b}".format(value)
    masked_value = "".join(mask[i] if mask[i] != "X" else binary[i] for i in range(len(mask)))
    return int(masked_value, 2)

def helper(binary_char, mask_char):
    if mask_char == "0":
        return binary_char
    elif mask_char == "1":
        return "1"
    else:
        return "X"

def expand(masked_value) -> List[int]:
    for i, char in enumerate(masked_value):
        if char == "X":
            return expand(masked_value[:i] + "0" + masked_value[i+1:]) + expand(masked_value[:i] + "1" + masked_value[i+1:])
    return [int(masked_value, 2)]

def mask_value_2(mask: str, idx: int):
    binary: str = "{:036b}".format(idx)
    masked_value = "".join(helper(binary[i], mask[i]) for i in range(len(mask)))
    val = expand(masked_value)
    return val


def part1(lines):
    mem = {}

    for line in lines:
        tmp = line.split(" = ")
        print(tmp)
        first, second = tmp[0], tmp[1]
        if first == "mask":
            mask = second
        else:
            idx = int(first[4:-1])
            value = int(second)
            masked_value = mask_value(mask, value)
            mem[idx] = masked_value

    return sum(mem.values())

def part2(lines):
    mem = {}

    for line in lines:
        tmp = line.split(" = ")
        print(tmp)
        first, second = tmp[0], tmp[1]
        if first == "mask":
            mask = second
        else:
            idx = int(first[4:-1])
            value = int(second)
            masked_indices = mask_value_2(mask, idx)
            for index in masked_indices:
                mem[index] = value

    return sum(mem.values())


if __name__ == "__main__":
    lines = read_input()
    res1 = part1(lines)
    print(f"part 1 answer: {res1}")
    res2 = part2(lines)
    print(f"part 2 answer: {res2}")