import collections
import re

def read_input():
    lines = []
    with open("dec07_input.txt", "r") as infile:
        for line in infile:
            lines.append(line.strip())
    return lines

def parse_children(children):
    # Remove . prefix
    children = children[:-1]
    if children == "no other bags":
        return []
    res = children.split(",")
    child_colors = []
    for item in res:
        item = item.strip()
        res = re.compile("^[0-9]+").match(item)
        assert res is not None, f"Searched '{item}', found nothing!"
        count = int(res.group())
        print(f"Searched '{item}', found count {count}")
        color = item[len(str(count)):].strip()
        if color[-1] != "s":
            color += "s"
        child_colors.append((count, color))
    return child_colors

def parse_bag(line):
    res = line.split("contain")
    print(res)
    color, children = res[0].strip(), res[1].strip()
    print(color, children)
    child_colors = parse_children(children)
    return color, child_colors

def size(bag, children, sizes):
    if bag in sizes:
        return sizes[bag]

    print(f"Searching {bag}, children are {children[bag]}")
    res = sum(count + count * size(child, children, sizes) for (count, child) in children[bag])
    sizes[bag] = res
    return res

def main(lines):
    children = {}
    for line in lines:
        color, child_colors = parse_bag(line)
        children[color] = child_colors

    print(children)

    parents = collections.defaultdict(list)
    for parent in children.keys():
        for child in children[parent]:
            parents[child].append(parent)

    # Part 1
    # start = "shiny gold bags"
    # to_visit = collections.deque([start])
    # seen = set()
    # while len(to_visit) > 0:
    #     current = to_visit.pop()
    #     print(f"Visiting {current}, with parents {parents[current]}")
    #     seen.add(current)
    #     for parent in parents[current]:
    #         if parent not in seen:
    #             to_visit.append(parent)
    # return len(seen) - 1 # Because the original one cannot contain itself

    # Part 2
    start = "shiny gold bags"
    return size(start, children, {})




if __name__ == "__main__":
    lines = read_input()
    res = main(lines)
    print(res)