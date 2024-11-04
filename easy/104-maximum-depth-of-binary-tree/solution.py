# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root: return 0

        max_l = self.maxDepth(root.left)
        max_r = self.maxDepth(root.right)

        return max(max_l, max_r) + 1