# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        queue = collections.deque([root])
        nodes = []

        while queue:
            rightmost = None

            for i in range(len(queue)):
                node = queue.popleft()

                if node:
                    rightmost = node.val

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            if rightmost or rightmost==0:
                nodes.append(rightmost)

        return nodes
                    