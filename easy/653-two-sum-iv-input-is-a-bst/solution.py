# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        
        seen = set()

        def search(node):
            if not node: return False
            
            diff = k - node.val
            
            if diff in seen:
                return True
            else:
                seen.add(node.val)
                return search(node.right) or search(node.left) 

        return search(root)
