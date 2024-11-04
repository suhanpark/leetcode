# [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)


## Problem Description

Given the `root` of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

![Description](./desc.jpg)

### Example 1:
```plaintext
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

### Example 2:
```plaintext
Input: root = [1,null,2]
Output: 2
```

### Constraints:
- The number of nodes in the tree is in the range `[0, 10^4]`.
- `100 <= Node.val <= 100`


## Solution

```python
# solution.py

def maxDepth(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    if not root: return 0

    max_l = self.maxDepth(root.left)
    max_r = self.maxDepth(root.right)

    return max(max_l, max_r) + 1
```

## Explanation
Complexity

Time: O(n)

Space: O(n)

We recursively calculate the depth of left and right subtree of each node, then take maximum of the depths.

## Results

The following graphs show the performance of the solution:

### Time Complexity
![Time Complexity](./time.png)

### Memory Usage
![Memory Usage](./space.png)