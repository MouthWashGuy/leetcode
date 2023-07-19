# Problem 238: Product of Array Except Self

# data structures

# helper functions

# test inputs
test1 = [1,2,3,4]

# solution here
def solution(nums):

    # note that this question is dp like, since the prefix product of element i is just the prefix product of element i-1 * i-1 itself
    # so we can actually just store it like before

    # idea: the product of elements without the ith term is just the product of the terms postfix and prefix subarrays
    # so we can just store the prefix products from i to n and then multiply them with their respective postfix products
    output_arr = [1]*len(nums)

    # first pass, calculating prefixes
    for i in range(1, len(nums)):
       output_arr[i] = output_arr[i - 1]*nums[i-1] # this is kind of like dp
    
    # second pass layering the post fix sums over the prefix sums
    # unfortunately we cant just throwing everything in the array this time cause were already storing prefixes there, so we need a temp var
    previous_postfix = 1
    for i in reversed(range(len(nums) - 1)):
        output_arr[i+1] = previous_postfix*output_arr[i+1]
        previous_postfix = previous_postfix*nums[i+1]

    # this loop doesnt run all the way to the 0th index for some reason so i guess we need to fill the gap outselves?
    # it makes sense considering we dont really calculate the postfix for the last term since we know its always 1
    output_arr[0] = output_arr[0]*previous_postfix
    
    return output_arr

    


# testing
if __name__ == "__main__":
    print(solution(test1))
