# Problem 2: Add Two Numbers

# data sructures
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# helper functions
def make_linked_list(nums):

    curr_node = None
    for i in range(len(nums)):
        if curr_node == None:
            curr_node = ListNode(nums[i])
            head = curr_node
        else:
            curr_node.next = ListNode(nums[i])
            curr_node = curr_node.next

    return head

def print_linked_list(list_node):

    output = ""

    while list_node != None:
        output += str(list_node.val)
        list_node = list_node.next

    return output
        
# test inputs
l1 = make_linked_list([2,4,3])
l2 = make_linked_list([5,6,4])

# solution here
def solution(l1, l2):
    
        carry = 0
        head = None
        curr_output_node = None

        while l1 != None or l2 != None:

            if l1 == None:
                val_sum = l2.val + 0 + carry
                l2 = l2.next
            elif l2 == None:
                val_sum = l1.val + 0 + carry
                l1 = l1.next
            else:
                val_sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next

            # okay heres the part where we account for overflows
            carry, quotient = divmod(val_sum, 10)

            # this only triggers once so we can return the head correctly
            if head == None:
                curr_output_node = ListNode(quotient)
                head = curr_output_node
            else:
                curr_output_node.next = ListNode(quotient)
                curr_output_node = curr_output_node.next

        # dont forget the carry can also be a value
        if carry != 0:
             curr_output_node.next = ListNode(carry)

        return head

# testing
if __name__ == "__main__":
    sol = solution(l1, l2)
    print(print_linked_list(sol))
    