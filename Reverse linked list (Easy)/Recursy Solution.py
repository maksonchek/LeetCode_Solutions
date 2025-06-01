# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        def rec(node, new_list):
            if node.next == None: #Базовый случай
                node.next = new_list
                return node
            next_node = node.next #Рекурсивный случай
            node.next = new_list
            new_list = node
            return rec(next_node, new_list)
        return rec(head, None)