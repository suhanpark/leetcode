# [112. Path Sum](https://leetcode.com/problems/path-sum/description/)


## Problem Description

Given the root of a binary tree and an integer `targetSum`, return `true` if the tree has a root-to-leaf path such that adding up all the values along the path equals `targetSum`.

A leaf is a node with no children.

![Description 1](./desc1.jpg)

### Example 1:
```plaintext
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
```
![Description 2](./desc2.jpg)

### Example 2:
```plaintext
Input: root = [1,2,3], targetSum = 5
Output: false
```

### Example 3:
```plaintext
Input: root = [], targetSum = 0
Output: false
```

### Constraints:
- The number of nodes in the tree is in the range `[0, 5000]`.
- `-1000 <= Node.val <= 1000`
- `-1000 <= targetSum <= 1000`


## Solution

```python
# solution.py

def hasPathSum(self, root, targetSum):
    """
    :type root: Optional[TreeNode]
    :type targetSum: int
    :rtype: bool
    """

    if not root:
        return False

    if not (root.left or root.right):
        return root.val == targetSum

    return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
```

## Explanation
Complexity

Time: O(n)

Space: O(n)

We recursively check the sum by checking if the complement exist in each node. 

## Results

The following graphs show the performance of the solution:

### Time Complexity
![Time Complexity](./time.png)

### Memory Usage
![Memory Usage](./space.png)