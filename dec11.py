import collections
import functools
import re

import numpy as np


def read_input():
    lines = []
    with open("dec11_input.txt", "r") as infile:
        for line in infile:
            lines.append(line.strip())
    return lines

def adjacent(arr, i, j):
    directions = [
        (-1,-1),
        (-1,0),
        (-1,1),
        (0,-1),
        (0,1),
        (1,-1),
        (1,0),
        (1,1),
    ]
    occupied = 0
    for d_i, d_j in directions:
        if 0 <= i+d_i < arr.shape[0] and 0 <= j+d_j < arr.shape[1]:
            if arr[i+d_i][j+d_j] == 2:
                occupied += 1
    return occupied

def adjacent2(arr, i, j):
    directions = [
        (-1,-1),
        (-1,0),
        (-1,1),
        (0,-1),
        (0,1),
        (1,-1),
        (1,0),
        (1,1),
    ]
    occupied = 0
    for d_i, d_j in directions:
        steps = 1
        while 0 <= i + steps * d_i < arr.shape[0] and 0 <= j + steps * d_j < arr.shape[1]:
            visible = arr[i + steps * d_i][j + steps * d_j]
            steps += 1
            if visible == 1:
                break
            elif visible == 2:
                occupied += 1
                break
    return occupied


def main(lines):
    # 0 = floor
    # 1 = empty
    # 2 = occupied
    rows = len(lines)
    cols = len(lines[0])

    arr = np.zeros((rows,cols))
    for i in range(rows):
        for j in range(cols):
            char = lines[i][j]
            if char == ".":
                arr[i][j] = 0
            elif char == "L":
                arr[i][j] = 1
            else:
                arr[i][j] = 2


    print(arr)
    print(arr.shape)

    iteration = 0
    while True:
        print(f"Iteration {iteration}")
        print(arr)
        arr_next = -1 * np.ones_like(arr)
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                if arr[i][j] == 0:
                    arr_next[i][j] = 0
                else:
                    neighbors = adjacent2(arr, i, j)
                    # print(f"location ({i},{j}) has {neighbors} neighbors")
                    if arr[i][j] == 1:
                        if neighbors == 0:
                            arr_next[i][j] = 2
                        else:
                            arr_next[i][j] = 1
                    else:
                        # Change to 4 for part 1
                        if neighbors >= 5:
                            arr_next[i][j] = 1
                        else:
                            arr_next[i][j] = 2
        if np.sum(arr_next - arr) == 0:
            break
        arr = arr_next
        iteration += 1

    occupied = np.sum(arr == 2)
    return occupied



if __name__ == "__main__":
    lines = read_input()
    res = main(lines)
    print(f"answer: {res}")