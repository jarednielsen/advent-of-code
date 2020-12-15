def part1(nums, highest):
    spoken = {}

    for i, num in enumerate(nums):
        spoken[num] = i

    num = nums[-1]
    age = 0
    for i in range(len(nums), highest):
        num = age
        # Calculate its age, then speak the number
        age = i - spoken[num] if num in spoken else 0
        spoken[num] = i
        print(f"{i}: Speaking {num}, with age {age}")  
    
    return num
           
            

if __name__ == "__main__":
    nums = [0,3,1,6,7,5]
    res1 = part1(nums, 2020)
    print(f"part 1 answer: {res1}")
    res2 = part1(nums, 30000000)
    print(f"part 2 answer: {res2}")
