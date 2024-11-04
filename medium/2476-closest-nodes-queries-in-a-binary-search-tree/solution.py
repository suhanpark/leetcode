# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution(object):
    def closestNodes(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[List[int]]
        """
        result = []
        tree = []
        def traverse(node, tree):
            if not node:
                return 
            
            traverse(node.left, tree)
            tree.append(node.val)
            traverse(node.right, tree)

        traverse(root, tree)
        
        for q in queries:
            result.append([-1, -1])
            l, r = 0, len(tree) - 1 
            
            while l <= r:
                mid = l + (r - l)//2

                if tree[mid] == q:
                    result[-1] = [q, q]
                    break
                elif tree[mid] > q:
                    result[-1][1] = tree[mid]
                    r = mid - 1
                elif tree[mid] < q:
                    result[-1][0] = tree[mid]
                    l = mid + 1

        return result

