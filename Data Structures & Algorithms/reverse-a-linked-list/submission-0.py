# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# input/output
# head = [0,1,2,3]
# output = [3,2,1,0]

# I would add a temporary node before the head of the list and then just flip the pointers,return the list

# point the head to a temp variable, 
# then the self.next (pointer) instead of pointing to the next one it needs to point to the previous one



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev




