# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root): # solution 1 BFS
        queue = collections.deque([root])
        result = []
        
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                
            if level:
                result.append(level)

        return result
    
    def levelOrder2(self, root): # solution 2 DFS
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        result = []

        def dfs(node, depth):
            if not node:
                return None

            if len(result) == depth:
                result.append([])

            result[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
         
        dfs(root, 0)
        return result

        
