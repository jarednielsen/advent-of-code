import collections
import functools
import re

import numpy as np


def read_input():
    lines = []
    with open("dec12_input.txt", "r") as infile:
        for line in infile:
            lines.append(line.strip())
    return lines


def main(lines):
    x, y = 0, 0 # starting location
    dx, dy = 1, 0 # direction we're facing
    for line in lines:
        action, value = line[0], int(line[1:])
        if action == "N":
            y += value
        elif action == "E":
            x += value
        elif action == "S":
            y -= value
        elif action == "W":
            x -= value
        elif action == "L" or action == "R":
            if action == "L":
                value = 360 - value

            if value == 90:
                dx, dy = dy, -dx
            elif value == 180:
                dx, dy = -dx, -dy
            elif value == 270:
                dx, dy = -dy, dx
            else:
                assert False, f"value={value}"
        elif action == "F":
            x += value * dx
            y += value * dy

    answer_1 = abs(x) + abs(y)
    return answer_1

def main(lines):
    x, y = 0, 0 # ship location
    wx, wy = 10, 1 # waypoint relative location
    for line in lines:
        action, value = line[0], int(line[1:])
        if action == "N":
            wy += value
        elif action == "E":
            wx += value
        elif action == "S":
            wy -= value
        elif action == "W":
            wx -= value
        elif action == "L" or action == "R":
            if action == "L":
                value = 360 - value

            while value > 0:
                wx, wy = wy, -wx
                value -= 90
        elif action == "F":
            x += value * wx
            y += value * wy

    answer_2 = abs(x) + abs(y)
    return answer_2



if __name__ == "__main__":
    lines = read_input()
    res = main(lines)
    print(f"answer: {res}")