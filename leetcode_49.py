# Problem 49: Group Anagrams

# data structures

# helper functions
# we need to sort each string by its chracters so that anagrams end up with the same key/hash
# easiest way to do this is to implement a simple counting sort, which will run in O(n) since we only have 26 chars
def counting_sort(string):

       output = ""

       # heres our static count array
       count_array = [0]*26

       # now we just populate it O(n)
       for char in string:
              count_array[ord(char) - 97] += 1

       # now we just reconstruct the sorted string
       for i in range(len(count_array)):
              for j in range(count_array[i]):
                     output += chr(i + 97)

       return output
                     

# test inputs
test1 = ["cat", "dog", "tac", "god", "act"]

# solution here
def solution(strs):

       # the key idea is that two strings when sorted, will be valid anagrams if they result in the same string after sorting
       # so we can use that sorted string as a key in a hashmap to group anagrams

       anagrams = {}

       for string in strs:

              # sort the string
              sorted_string = counting_sort(string)

              # now check the hashmap for membership
              if sorted_string not in anagrams:
                     anagrams[sorted_string] = []

              anagrams[sorted_string].append(string)
              
       output = []
       for group in anagrams.values():
              output.append(group)

       return output

# testing
if __name__ == "__main__":
       print(solution(test1))       
       
