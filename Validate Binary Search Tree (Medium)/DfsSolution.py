# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            
            return rec(node.left, left, node.val) and rec(node.right, node.val, right)
        return rec(root, float('-inf'), float('inf'))