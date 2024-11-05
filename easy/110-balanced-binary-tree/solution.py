# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(node):
            if not node:
                return [True, 0]
            
            l = dfs(node.left)
            r = dfs(node.right)

            balanced = l[0] and r[0] and abs(l[1]-r[1]) <= 1
            return [balanced, max(l[1], r[1])+1]

        return dfs(root)[0]
