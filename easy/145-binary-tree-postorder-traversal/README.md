# [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/description/)


## Problem Description

Given the root of a binary tree, return the postorder traversal of its nodes' values.

![Description 1](./desc1.jpg)

### Example 1:
```plaintext
Input: root = [1,null,2,3]
Output: [3,2,1]
```
![Description 2](./desc2.jpg)

### Example 2:
```plaintext
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,6,7,5,2,9,8,3,1]
```

### Example 3:
```plaintext
Input: root = []
Output: []
```

### Example 4:
```plaintext
Input: root = [1]
Output: [1]
```

### Constraints:
- The number of the nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`


## Solution

```python
# solution.py

def postorderTraversal(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """
    result = []

    def pot(node):
        if not node: 
            return

        pot(node.left)
        pot(node.right)
        result.append(node.val)

    pot(root)
    return result
```

## Explanation
Complexity

Time: O(n)

Space: O(n)

We recursively perform postorder traversal (left, right, root).

## Results

The following graphs show the performance of the solution:

### Time Complexity
![Time Complexity](./time.png)

### Memory Usage
![Memory Usage](./space.png)