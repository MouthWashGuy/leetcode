# Problem 347: Top K Frequent Elements

# imports
import heapq

# data structures
class HeapNode():

       def __init__(self, key, count):
              self.key = key
              self.count = count
       
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
test3 = [1,1,1,2,2,3,3,3,3,3,3,3,3,3,3,0]
test4 = [2,2,2,1,3,3]

# solution here
def solution(nums, k):

       # first we have to build a map of each number, to its associated frequency, we could use an array to do this, but that would require knowing the max of the array nums
       # hence a hashmap can be used instead
       count_map = {}
       for num in nums:
              count_map[num] = count_map.get(num, 0) + 1 # using get here saves us some time, as it allows us to use 0 as a default value whenever we see a number for this first time

       # now the magic happens, since we have a nice map of numbers:frequency we can use a heap to gather up the most frequent numbers
       # this is achieved by using a heap of size k, by using a minheap, the least frequent element is always the root of the heap
       # hence, by iterating over the map, and comparing the count of the ith item to the heaps root, we can know if that item belong in the heap at all
       # since everything below the root as a greater count than it, we do not need to bother with further comparisons.
       heap = []

       for num, count in list(count_map.items()):

              # insert simply
              if len(heap) < k:
                     heapq.heappush(heap, HeapNode(num, count))
              elif count > heap[0].count:
                     heapq.heapreplace(heap, HeapNode(num, count))

       return [node.key for node in heap]
              
# testing
if __name__ == "__main__":
       print(solution(test3, 3))
       print(solution(test4, 2))
       print(solution(test2, 2))
       
