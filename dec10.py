import collections
import functools
import re

import numpy as np


def read_input():
    lines = []
    with open("dec10_input.txt", "r") as infile:
        for line in infile:
            lines.append(int(line.strip()))
    return lines

@functools.lru_cache(maxsize=None)
def arrangements(index):
    """ Return the number of ways to count up by a max of 3. """
    print(f"Calling arrangements({index})")
    if index == len(adapters) - 1:
        print(f"arrangements({index}) = 1")
        return 1
    else:
        count = 0
        for i in range(index+1, index+4):
            if i == len(adapters):
                count += 1
                break
            if adapters[i] - adapters[index] <= 3:
                count += arrangements(i)
        print(f"arrangements({index}) = {count}")
        return count


def main(lines):
    global adapters
    adapters = np.array(sorted(lines))
    print(f"len(adapters)={len(adapters)}")
    # print(adapters)
    # diffs = adapters - np.concatenate((np.array([0]), adapters[:-1]))
    # print(diffs)
    # counts = collections.Counter(diffs)
    # counts[3] += 1 # for the built-in adapter
    # print(f"answer = {counts[1] * counts[3]}")
    return arrangements(0)



if __name__ == "__main__":
    lines = read_input()
    res = main(lines)
    print(f"answer: {res}")