import heapq as h
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        head = ListNode()
        root = head
        for i, l in enumerate(lists):
            if l:
                h.heappush(heap, (l.val, i, l))
        while heap:
            val, i, node = h.heappop(heap)
            head.next = node
            head = head.next
            if node.next:
                h.heappush(heap, (node.next.val, i, node.next))
        return root.next
