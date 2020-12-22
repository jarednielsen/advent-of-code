import argparse
import collections

def read_lines(filename):
    lines = []
    with open(filename) as infile:
        for line in infile:
            lines.append(line.strip())
    return lines

def is_operator(char):
    return char in {"+", "*"}

def reduce(stack, fully: bool = False):
    """ Simplify the stack if it ends in an ")" or multiplication operator"""
    while len(stack) > 1:
        char = stack[-1]
        if char in {"(", "+", "*"}:
            break
        elif char == ")":
            stack.pop()
            # Backtrack to open parenthesis, then solve that subsection
            inside = []
            val = None
            while True:
                val = stack.pop()
                if val == "(":
                    break
                else:
                    inside.append(str(val))
            res = solve(inside[::-1])
            stack.append(res)
        else:
            # Last element is digit
            # Check if second-to-last element is multiplication; if so, reduce
            if len(stack) == 1:
                break
            else:
                # if is_operator(stack[-2]):
                if stack[-2] == "+" or (stack[-2] == "*" and fully):
                    val2 = stack.pop()
                    operator = stack.pop()
                    val1 = stack.pop()
                    res = val1 * val2 if operator == "*" else val1 + val2
                    stack.append(res)
                else:
                    break



def solve(tokens):
    # Iterate over the string
    # At each character, add it to the stack or pop off a result off the stack
    # When you see a closing parenthesis, pop it off the stack until you come to the opening
    # When you see a number, add it to the stack if it is the first, or pop until you can reduce
    pretty_tokens = " ".join(tokens)
    print(f"Solving '{pretty_tokens}'")
    stack = collections.deque()
    for char in tokens:
        print(f"Stack is {stack}, viewing char '{char}'")
        if char.isdigit():
            char = int(char)
        stack.append(char)
        reduce(stack)
    reduce(stack, fully=True)

    assert len(stack) == 1, f"stack={stack}"
    print(f"Solution to '{pretty_tokens}' is '{stack[0]}'")
    return stack[0]




def main(lines):
    answers = []
    for line in lines:
        if not line.startswith("#"):
            answer = solve(list(line.replace(" ", "")))
            answers.append(answer)

    print(f"answers are: \n{answers}\n")
    return sum(answers)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", default="dec18_test.txt")
    args = parser.parse_args()

    lines = read_lines(args.filename)
    res = main(lines)
    print(f"answer: {res}")