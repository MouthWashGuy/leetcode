# Problem 217: Contains Duplicate 

# data structures

# helper functions

# test inputs
arr1 = [1,2,3,1]
arr2 = [1,2,3,4]

# solution here
def solution(nums):

       # im not sure if theres a faster way to do this than O(n)
       # but in theory we could just use a hashmap to keep track of all the values and return when we discover a duplicate
       seen = {}

       for num in nums:
              if num in seen:
                     return True
              else:
                     seen[num] = True

       return False
       
# testing
if __name__ == "__main__":
       print(solution(arr1))
       print(solution(arr2))
       
