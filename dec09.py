import collections
import re

def read_input():
    lines = []
    with open("dec09_input.txt", "r") as infile:
        for line in infile:
            lines.append(int(line.strip()))
    return lines

def is_two_sum(seen, target):
    for i in range(len(seen)):
        for j in range(len(seen)):
            if i != j:
                if seen[i] + seen[j] == target:
                    return True
    return False

# def main(lines):
#     preamble = 25
#     for i, line in enumerate(lines):
#         if i < preamble:
#             continue
#         if is_two_sum(lines[i-25:i], line):
#             continue
#         else:
#             print(f"Failed, current val is {line}")

def main(lines):
    target = 1124361034
    start, end = 0, 0
    cur_sum = 0
    while True:
        if sum(lines[start:end]) < target:
            end += 1
        elif sum(lines[start:end]) > target:
            start += 1
        else:
            print(f"Success, start={start}, end={end}")
            break

    largest = max(lines[start:end])
    smallest = min(lines[start:end])
    print(f"largest={largest}, smallest={smallest}")
    total = largest + smallest
    print(f"answer={total}")



if __name__ == "__main__":
    lines = read_input()
    res = main(lines)
    print(res)