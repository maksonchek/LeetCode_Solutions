# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        def merge(list1, list2):
            if not list1:
                return list2
            if not list2:
                return list1
            if list1.val <= list2.val:
                list1.next = merge(list1.next, list2)
                return list1
            else:
                list2.next = merge(list1, list2.next)
                return list2
            
        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists)-interval, interval*2):
                lists[i] = merge(lists[i], lists[i+interval])
            interval*=2
        return lists[0]