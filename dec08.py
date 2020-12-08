import collections
import re

def read_input():
    lines = []
    with open("dec08_input.txt", "r") as infile:
        for line in infile:
            lines.append(line.strip())
    return lines

def successful(lines, flip):
    """ Flip the line at index `flip`. """
    seen = set()
    i = 0
    acc = 0
    n_nops = 0
    n_jmps = 0
    while i not in seen and i < len(lines):
        seen.add(i)
        res = lines[i].split(" ")
        cmd, val = res[0], int(res[1])
        if i == flip:
            if cmd == "nop":
                cmd = "jmp"
            elif cmd == "jmp":
                cmd = "nop"

        if cmd == "nop":
            i += 1
            n_nops += 1
        elif cmd == "acc":
            acc += val
            i += 1
        elif cmd == "jmp":
            i += val
            n_jmps += 1

    print(f"nops: {n_nops}, jmps: {n_jmps}")
    if i == len(lines):
        return acc, True
    else:
        return acc, False

def main(lines):
    for i in range(0, len(lines)):
        acc, success = successful(lines, i)
        print(f"Flip {i}: acc {acc}, success {success}")
        if success:
            return acc


if __name__ == "__main__":
    lines = read_input()
    res = main(lines)
    print(res)