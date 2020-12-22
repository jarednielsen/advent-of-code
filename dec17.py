import argparse
import itertools

import numpy as np

def read_lines(filename):
    lines = []
    with open(filename) as infile:
        for line in infile:
            lines.append(line.strip())
    return lines

def locs(shape):
    """
    Return a list of all integer locations within the n-dimensional box described by shape.

    So locs((2, 2)) -> [(0,0), (0,1), (1,0), (1,1)] with order not preserved.
    """
    return list(itertools.product(*(range(dim) for dim in shape)))

# Dimension-independent
def active_neighbors(arr, loc):
    dims = len(loc)

    count = 0
    increments = locs(3 for _ in range(dims))
    increments = [tuple(d-1 for d in inc) for inc in increments if not all(d == 1 for d in inc)]
    for inc in increments:
        loc_inc = tuple(d_loc + d_inc for (d_loc, d_inc) in zip(loc, inc))
        if all((0 <= d < size) for (d, size) in zip(loc_inc, arr.shape)):
            if arr[loc_inc] == 1:
                count += 1

    return count

# Dimension-independent
def neighbors_arr(arr):
    arr_new = np.zeros_like(arr)
    for loc in locs(arr.shape):
        neighbors = active_neighbors(arr, loc)
        arr_new[loc] = neighbors
    return arr_new

# Dimension-independent
def update(arr, neighbors):
    """ Modify `arr` in-place."""
    for loc in locs(arr.shape):
            n = neighbors[loc]
            if arr[loc] == 0:
                arr[loc] = 1 if n == 3 else 0
            else:
                arr[loc] = 1 if (n == 2 or n == 3) else 0

def main(lines):
    # We'll represent the data as an array of NumPy arrays of 0's and 1's
    n = len(lines)
    z = 1
    shape = (z, z, n, n)
    dim = len(shape)
    assert dim in {3, 4}
    arr = np.zeros(shape, dtype=int)
    plane = np.zeros((n,n), dtype=int)
    for i,j in itertools.product(range(n), range(n)):
    # for i in range(n):
    #     for j in range(n):
        plane[i,j] = 1 if lines[i][j] == "#" else 0

    if dim == 3:
        arr[0] = plane
    elif dim == 4:
        arr[0,0] = plane

    print(f"arr at init: \n{arr}\n")

    for cycle in range(1, 7):
        shape_new = tuple(d+2 for d in shape)
        print(f"shape={shape}, shape_new={shape_new}")
        arr_new = np.zeros(shape_new, dtype=int)
        print(f"arr shape: {arr.shape}")
        print(f"arr_new shape: {arr_new.shape}")
        if dim == 3:
            arr_new[1:-1,1:-1,1:-1] = arr
        elif dim == 4:
            arr_new[1:-1,1:-1,1:-1,1:-1] = arr
        neighbor_count = neighbors_arr(arr_new)
        print(f"arr before cycle {cycle}: \n{arr}\n")
        print(f"resized arr_new before cycle: \n{arr_new}\n")
        print(f"neighbor_count: \n{neighbor_count}\n")
        update(arr_new, neighbor_count)

        arr = arr_new
        shape = shape_new

        # arr_new[z+1,i+1,j+1] refers to arr[z,i,j]
        print(f"arr after cycle {cycle}: \n{arr}\n")

        active_cubes = np.sum(arr)
        print(f"Cubes after {cycle} cycles: {active_cubes}")

    return active_cubes




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", default="dec17_input.txt")
    args = parser.parse_args()

    lines = read_lines(args.filename)
    res1 = main(lines)
    print(f"answer={res1}")