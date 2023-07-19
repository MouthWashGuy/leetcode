# Problem 3: Longest Substring Without Repeating Characters

# data structures

# helper functions

# test inputs
s1 = "aab"
s2 = "abcabcbb"
s3 = "bbbbbbb"
s4 = "abba"

# solution here
def solution(s):

       left = 0
       right = 0
       max_substring_length = 0

       # we can use an array here to track the last seen index of each character we see
       # works like a hashmap basically, the mapping is ord(char): last seen index
       chars = [None]*128

       while right < len(s):

              curr_char = ord(s[right])

              if chars[curr_char] != None:
                     if chars[curr_char] >= left: # this is to make sure we disregard indexes outside the window
                            max_substring_length = max(right - left, max_substring_length)
                            left = chars[curr_char] + 1

              chars[curr_char] = right
              right += 1

       return max(right - left, max_substring_length)

# testing
if __name__ == "__main__":
       print(solution(s1))
       print(solution(s2))
       print(solution(s3))
       print(solution(s4))
       
