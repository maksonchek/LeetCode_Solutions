# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        cur_node = head
        next_node = head.next
        new_end = None
        while cur_node.next != None:
            cur_node.next = new_end
            new_end = cur_node
            cur_node = next_node
            next_node = next_node.next
        cur_node.next = new_end
        return cur_node