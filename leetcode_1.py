# Problem 1: Two Sum

# test inputs
nums = [2, 7, 11, 15]
target = 9


# solution here
def solution(nums, target):
    # we use a hashmap to store each number in nums as a key, and its associated index position in nums as a value
    num_to_idx = {}

    # iterate over each number, subtracting it from target. If we can find its compliment in the hashmap,
    # we will have two numbers that add up to target
    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in num_to_idx:
            return num_to_idx[compliment], i
        else:
            num_to_idx[nums[i]] = i


# testing
if __name__ == "__main__":
    print(solution(nums, target))
