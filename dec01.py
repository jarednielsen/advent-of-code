

def read_input():
    nums = []
    with open("dec01_input.txt", "r") as infile:
        for line in infile:
            nums.append(int(line))
    return nums

def twosum(nums):
    target = 2020
    seen = set()
    for num in nums:
        if target - num in seen:
            return num, target - num
        seen.add(num)
    assert False, "Didn't find a solution"

def threesum(nums):
    true_target = 2020
    for i, n1 in enumerate(nums):
        seen = set()
        target = true_target - n1
        for j, n2 in enumerate(nums):
            if i != j:
                if target - n2 in seen:
                    return n1, n2, target - n2
                seen.add(n2)
    assert False, "Didn't find a solution"

if __name__ == "__main__":
    nums = read_input()
    # n1, n2 = twosum(nums)
    # print(n1 * n2)
    n1, n2, n3 = threesum(nums)
    print(n1, n2, n3)
    print(n1 * n2 * n3)