# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tree = []
        
        def dfs(node):
            if not node: return

            dfs(node.left)
            tree.append(node.val)
            dfs(node.right)

        def percolate(left, right):
            if left > right: return None

            mid = (left + right) // 2
            return TreeNode(tree[mid], percolate(left, mid-1), percolate(mid+1, right))

        dfs(root)

        return percolate(0, len(tree)-1)
        

