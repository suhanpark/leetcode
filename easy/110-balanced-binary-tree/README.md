# [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/)


## Problem Description

Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

![Description 1](./desc1.jpg)

### Example 1:
```plaintext
Input: root = [3,9,20,null,null,15,7]
Output: true
```

![Description 1](./desc1.jpg)

### Example 2:
```plaintext
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
```

### Example 3:
```plaintext
Input: root = []
Output: true
```

### Constraints:
- The number of nodes in the tree is in the range `[0, 5000]`.
- `-10^4 <= Node.val <= 10^4`


## Solution

```python
# solution.py

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
```

## Explanation
Complexity

Time: O(n)

Space: O(n)

We recursively perform depth-first search and find the depth of left and right subtrees of each node.

## Results

The following graphs show the performance of the solution:

### Time Complexity
![Time Complexity](./time.png)

### Memory Usage
![Memory Usage](./space.png)