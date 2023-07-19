# Problem 347: Top K Frequent Elements

# imports
import heapq

# data structures
class HeapNode():

       def __init__(self, key):
              self.key = key
              self.count = 0
       
       def __lt__(self, other):
              return self.count < other.count

       def __le__(self, other):
              return self.count <= other.count

       def __gt__(self, other):
              return self.count > other.count

       def __ge__(self, other):
              return self.count >= other.count

       def __eq__(self, other):
              return self.count == other.count

       def __ne__(self, other):
              return self.count != other.count
       
# helper functions

# test inputs
test1 = [1,1,1,2,2,3]
test2 = [3,3,3,1,1,2]
test3 = [1,1,1,2,3,3,3,3,3,3,3,3,3,3,0]
test4 = [2,2,2,1,3,3]

# solution here
def solution(nums, k):

      # first we do one pass over the array to count the occurences of each element
      count_map = {}
      for num in nums:
             
             # if we havent seen it before
             if num not in count_map:
                    count_map[num] = HeapNode(num)
                    
             count_map[num].count -= 1

       # Theres actually a better version of the algorithm where we can maintain a heap of size k, and then iterate over the elements in the dictionary, adding them to the heap.
       # with a min heap, the least frequent element is always the root of the heap, hence, by comparing every elment to the root, we can know quickly if that element should enter the heap or not
       # TODO

      # this should populate our hashmap nicely
      dict_items = list(count_map.values())
      heapq.heapify(dict_items)
      
      # now we return k items
      output = []
      for i in range(k):
             output.append(heapq.heappop(dict_items).key)

      return output
             

# testing
if __name__ == "__main__":
       print(solution(test3, 2))
       print(solution(test4, 2))
       print(solution(test2, 2))
       
