# [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/description/)


## Problem Description

Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.


![Description 1](./desc1.jpg)

### Example 1:
```plaintext
Input: root = [2,1,3]
Output: true
```

![Description 2](./desc2.jpg)

### Example 2:
```plaintext
Input: root = [5,1,4,null,null,3,6]
Output: false
```

### Constraints:
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-2^31 <= Node.val <= 2^31 - 1`


## Solution

```python
# solution.py

def isValidBST(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """

    def check(node, left, right):
        if not node: return True

        if not (left < node.val < right):
            return False

        return check(node.left, left, node.val) and check(node.right, node.val, right)

    return check(root, float('-inf'), float('inf'))
```

## Explanation
Complexity

Time: O(n)

Space: O(n)

We recursively pass left and right value to check the conditional where the parent is in between left and right values. In order to validate the whole tree, we have to make sure both left and right sides are valid.

## Results

The following graphs show the performance of the solution:

### Time Complexity
![Time Complexity](./time.png)

### Memory Usage
![Memory Usage](./space.png)