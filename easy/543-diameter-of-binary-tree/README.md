# [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/description/)


## Problem Description

Given the `root` of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The length of a path between two nodes is represented by the number of edges between them.

![Description](./desc.jpg)

### Example 1:
```plaintext
Input: root = [1,2,3,4,5]
Output: 3
```

### Example 2:
```plaintext
Input: root = [1,2]
Output: 1
```

### Constraints:
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-100 <= Node.val <= 100`


## Solution

```python
# solution.py

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
```

## Explanation
Complexity

Time: O(n)

Space: O(n)

We recursively perform depth-first search and update the diameter `d`.

## Results

The following graphs show the performance of the solution:

### Time Complexity
![Time Complexity](./time.png)

### Memory Usage
![Memory Usage](./space.png)