# Problem 242: Valid Anagram

# data structures

# helper functions

# test inputs
s = "anagram"
t = "nagaram"

# solution here
def solution(s, t):

       # first check if they are of the same length
       if len(s) != len(t):
              return False

       # we can use a static array to keep track of the letter count for each character
       character_count_s = [0] * 26
       character_count_t = [0] * 26

       for i in range(len(s)):
              character_count_s[ord(s[i]) - 97] += 1
              character_count_t[ord(t[i]) - 97] += 1

       for i in range(26):
              if character_count_s[i] != character_count_t[i]:
                     return False

       return True

       # theres a smarter approach where we dont need two array, we can just use one
       # in this case we plus and minus so the overall chracter count should balance to 0 if the strings are an anagram
       

# testing
if __name__ == "__main__":
       print(solution(s, t))     
