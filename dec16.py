import argparse
import copy

def get_lines(filename):
    lines = []
    with open(filename) as infile:
        for line in infile:
            lines.append(line.strip())
    return lines

def valid_numbers(condition_str):
    """ Returns a set of valid numbers. """
    nums = set()
    conditions = condition_str.split(" or ")
    for cond_str in conditions:
        lohi = cond_str.split("-")
        lo, hi = int(lohi[0]), int(lohi[1])
        for i in range(lo, hi+1):
            nums.add(i)
    return nums



def parse_lines(lines):
    """ Returns a tuple of (conditions, your ticket, nearby tickets) """
    conditions = {}
    i = 0
    while lines[i] != "":
        res = lines[i].split(": ")
        name, condition_str = res[0], res[1]
        conditions[name] = valid_numbers(condition_str)
        i += 1

    # Pass over the "your ticket" line
    i += 2
    yours = [int(num) for num in lines[i].split(",")]

    i += 3

    nearby = []
    while i < len(lines):
        nearby.append([int(num) for num in lines[i].split(",")])
        i += 1

    return conditions, yours, nearby

def main(lines):
    conditions, yours, nearby = parse_lines(lines)
    nums_union = set().union(*conditions.values())
    print(f"nums_union={nums_union}")

    valid_tickets = []
    invalid_nums = []
    for ticket in [yours] + nearby:
        is_valid = True
        for num in ticket:
            if num not in nums_union:
                invalid_nums.append(num)
                is_valid = False
        if is_valid:
            valid_tickets.append(ticket)

    print(f"invalid_nums={invalid_nums}")
    print(f"valid_tickets={valid_tickets}")

    n_fields = len(conditions)
    mappings = {i: set(conditions.keys()) for i in range(n_fields)}

    for ticket in valid_tickets:
        for j, num in enumerate(ticket):
            # Check all mappings
            to_remove = set()
            for name in mappings[j]:
                if num not in conditions[name]:
                    to_remove.add(name)
            mappings[j] = mappings[j].difference(to_remove)

    print(mappings)

    final_mappings = {}
    while len(final_mappings) < n_fields:
        # print(mappings)
        # print(f"Final: {final_mappings}")
        for i, names in mappings.items():
            # print(f"Viewing {i}, {names}")
            if len(names) == 1:
                final_mappings[i] = list(names)[0]
            else:
                to_remove = set()
                for name in names:
                    if name in final_mappings.values():
                        to_remove.add(name)
                mappings[i] = names.difference(to_remove)

    print(mappings)
    print(final_mappings)

    res = 1
    for i, name in final_mappings.items():
        if name.startswith("departure"):
            print(f"{name} = {yours[i]}")
            res *= yours[i]

    # return sum(invalid)
    return res

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", type=str, default="dec16_input.txt")
    args = parser.parse_args()

    lines = get_lines(args.filename)
    res = main(lines)
    print(f"answer: {res}")