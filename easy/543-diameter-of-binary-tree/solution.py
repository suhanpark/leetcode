# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        d = 0
        def dfs(node):
            if not node: return 0
            nonlocal d
            
            l = dfs(node.left)
            r = dfs(node.right)
            d = max(l+r, d)
            return max(l, r) + 1

        dfs(root)
        return d