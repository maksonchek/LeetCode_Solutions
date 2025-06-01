# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        prev = set()
        def isCycle(node):
            if node:
                if node in prev:
                    return True
                else:
                    prev.add(node)
                    return isCycle(node.next)
            else:
                return False
        return isCycle(head)
                    
            