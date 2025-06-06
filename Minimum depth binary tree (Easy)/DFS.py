# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftD = self.minDepth(root.left)
        rightD = self.minDepth(root.right)

        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return 1 + rightD
        if root.right is None:
            return 1 + leftD
        return min(leftD, rightD) + 1