# [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/description/)


## Problem Description

Given the `root` of a binary tree, invert the tree, and return its `root`.

![Description 1](./desc1.jpg)

### Example 1:
```plaintext
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```
![Description 2](./desc2.jpg)

### Example 2:
```plaintext
Input: root = [2,1,3]
Output: [2,3,1]
```

### Example 3:
```plaintext
Input: root = []
Output: []
```

### Constraints:
- The number of the nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`


## Solution

```python
# solution.py

def invertTree(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: Optional[TreeNode]
    """
    def swap(node):
        if not node: return

        node.left, node.right = node.right, node.left

        swap(node.left)
        swap(node.right)

    swap(root)
    return root
```

## Explanation
Complexity

Time: O(n)

Space: O(n)

We recursively perform preorder traversal (left, root, right), then swap left and right children.

## Results

The following graphs show the performance of the solution:

### Time Complexity
![Time Complexity](./time.png)

### Memory Usage
![Memory Usage](./space.png)